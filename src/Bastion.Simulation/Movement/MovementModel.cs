using Bastion.Simulation.Movement.Geometry;

namespace Bastion.Simulation.Movement;

/// <summary>
/// Marche sur terrain plat (MEC-0003) pour une carte, un barème et une emprise d'unité donnés.
/// Les calculs de zone et de chemin ne modifient rien ; un pas ne produit un nouvel état que si tous
/// ses contrôles réussissent (A9).
/// </summary>
public sealed class MovementModel
{
    private readonly StepGeometry _geometry;
    private readonly Dictionary<(GridPosition Cell, Direction Orientation, Direction Step), StepPlan> _plans = new();

    public MovementModel(TacticalMap map, MovementRules rules, UnitBody body)
    {
        Map = map ?? throw new ArgumentNullException(nameof(map));
        Rules = rules ?? throw new ArgumentNullException(nameof(rules));
        Body = body ?? throw new ArgumentNullException(nameof(body));
        _geometry = new StepGeometry(map, body);
    }

    public TacticalMap Map { get; }

    public MovementRules Rules { get; }

    public UnitBody Body { get; }

    /// <summary>
    /// Crée l'état d'une unité après avoir vérifié qu'il est admissible : case de la carte, non
    /// infranchissable, ressources positives ou nulles, emprise au repos sans chevauchement.
    /// </summary>
    public UnitState CreateState(GridPosition position, Direction orientation, int tu, int energy)
    {
        if (!Map.Contains(position))
        {
            throw new ArgumentException($"Position initiale non admissible : la case {position} est hors de la carte.", nameof(position));
        }

        if (Map.IsBlocked(position))
        {
            throw new ArgumentException($"Position initiale non admissible : la case {position} est infranchissable.", nameof(position));
        }

        if (tu < 0 || energy < 0)
        {
            throw new ArgumentException($"Les TU et l'énergie ne peuvent pas être négatives ; reçu : {tu} TU, {energy} d'énergie.", nameof(tu));
        }

        if (!_geometry.RestIsFree(position, orientation))
        {
            throw new ArgumentException(
                $"Position initiale non admissible : en {position}, orientée {orientation}, l'emprise de l'unité chevauche un obstacle.",
                nameof(position));
        }

        return new UnitState(position, orientation, tu, energy);
    }

    /// <summary>
    /// Évalue un pas depuis l'état donné, sans le modifier. Tous les contrôles (rotation, passage,
    /// coût réel et ressources) précèdent toute modification : si l'un échoue, l'état rendu est
    /// l'état initial, inchangé (A9).
    /// </summary>
    public StepOutcome EvaluateStep(UnitState state, Direction direction)
    {
        ArgumentNullException.ThrowIfNull(state);
        StepPlan plan = PlanStep(state.Position, state.Orientation, direction);
        if (plan.Refusal != StepRefusal.None)
        {
            return new StepOutcome(direction, plan.Refusal, plan.Cost, RotationSense.None, null, state);
        }

        StepCost cost = plan.Cost!.Value;
        if (cost.Tu > state.Tu)
        {
            return new StepOutcome(direction, StepRefusal.InsufficientTu, cost, RotationSense.None, null, state);
        }

        if (cost.Energy > state.Energy)
        {
            return new StepOutcome(direction, StepRefusal.InsufficientEnergy, cost, RotationSense.None, null, state);
        }

        UnitState next = state with
        {
            Position = state.Position.Step(direction),
            Orientation = direction,
            Tu = state.Tu - cost.Tu,
            Energy = state.Energy - cost.Energy,
        };
        return new StepOutcome(direction, StepRefusal.None, cost, plan.Rotation, plan.Passage, next);
    }

    /// <summary>Zone atteignable et meilleurs chemins depuis l'état donné (Z1, G3, G4, Q4.16). Ne modifie rien.</summary>
    public Reachability ComputeReachability(UnitState state)
    {
        ArgumentNullException.ThrowIfNull(state);
        return PathSearch.Run(this, state);
    }

    /// <summary>
    /// Exécute un chemin pas à pas. Le premier pas refusé arrête l'ordre, sans nouveau calcul de
    /// chemin (Q3.4, Q4.21) ; les pas déjà exécutés gardent leurs effets et leurs coûts (A9).
    /// Le coût de chaque pas est son coût réel sur cette carte (M-05).
    /// </summary>
    public PathOutcome ExecutePath(UnitState state, IReadOnlyList<Direction> path)
    {
        ArgumentNullException.ThrowIfNull(state);
        ArgumentNullException.ThrowIfNull(path);
        var outcomes = new List<StepOutcome>();
        UnitState current = state;
        foreach (Direction direction in path)
        {
            StepOutcome outcome = EvaluateStep(current, direction);
            outcomes.Add(outcome);
            if (!outcome.Accepted)
            {
                break;
            }

            current = outcome.State;
        }

        return new PathOutcome(current, outcomes);
    }

    /// <summary>
    /// Ordre vers une destination : refusé si elle n'appartient pas à la zone atteignable (Z1) ; sinon,
    /// exécution du chemin choisi selon G4 et Q4.16.
    /// </summary>
    public OrderOutcome ExecuteOrder(UnitState state, GridPosition destination)
    {
        Reachability reachability = ComputeReachability(state);
        if (!reachability.TryGetPath(destination, out PlannedPath? path))
        {
            return new OrderOutcome(destination, null, null, state);
        }

        PathOutcome execution = ExecutePath(state, path.Steps);
        return new OrderOutcome(destination, path, execution, execution.FinalState);
    }

    /// <summary>Contrôles d'un pas qui ne dépendent pas des ressources, mis en cache par carte.</summary>
    internal StepPlan PlanStep(GridPosition from, Direction orientation, Direction direction)
    {
        var key = (from, orientation, direction);
        if (!_plans.TryGetValue(key, out StepPlan? plan))
        {
            plan = ComputeStepPlan(from, orientation, direction);
            _plans[key] = plan;
        }

        return plan;
    }

    private StepPlan ComputeStepPlan(GridPosition from, Direction orientation, Direction direction)
    {
        GridPosition to = from.Step(direction);
        if (!Map.Contains(to))
        {
            return StepPlan.Refused(StepRefusal.OutsideMap, null);
        }

        StepCost cost = Rules.CostOf(direction, Map.TerrainAt(to));
        if (Map.IsBlocked(to))
        {
            return StepPlan.Refused(StepRefusal.ArrivalBlocked, cost);
        }

        // 1. Rotation vers le pas engagé (Q4.17), au centre de la case de départ (A5, A7).
        RotationSense rotation = RotationSense.None;
        int eighths = RotationRules.ClockwiseEighths(orientation, direction);
        if (eighths == 4)
        {
            bool clockwiseFree = _geometry.RotationIsFree(from, orientation, direction, RotationSense.Clockwise);
            bool counterClockwiseFree = !clockwiseFree
                && _geometry.RotationIsFree(from, orientation, direction, RotationSense.CounterClockwise);
            RotationSense? chosen = RotationRules.ChooseHalfTurn(clockwiseFree, counterClockwiseFree);
            if (chosen is null)
            {
                return StepPlan.Refused(StepRefusal.RotationBlocked, cost);
            }

            rotation = chosen.Value;
        }
        else if (eighths != 0)
        {
            // Rotation de 45°, 90° ou 135° : du côté le plus court (A5).
            rotation = eighths < 4 ? RotationSense.Clockwise : RotationSense.CounterClockwise;
            if (!_geometry.RotationIsFree(from, orientation, direction, rotation))
            {
                return StepPlan.Refused(StepRefusal.RotationBlocked, cost);
            }
        }

        // 2. Passage et volume le long du trajet (G1, A2, A3).
        if (!direction.IsDiagonal())
        {
            if (Map.WallBetween(from, direction) is not null)
            {
                return StepPlan.Refused(StepRefusal.WallOnEdge, cost);
            }

            return _geometry.TranslationIsFree(from, to, direction)
                ? StepPlan.Admitted(cost, rotation, null)
                : StepPlan.Refused(StepRefusal.VolumeCollision, cost);
        }

        (Direction first, Direction second) = direction.Passages();
        foreach (Direction passage in new[] { first, second })
        {
            if (PassageIsPracticable(from, passage, to, direction))
            {
                return StepPlan.Admitted(cost, rotation, passage);
            }
        }

        return StepPlan.Refused(StepRefusal.NoPracticablePassage, cost);
    }

    /// <summary>
    /// Passage orthogonal d'un pas diagonal : ouvert au sens de S3 et N2 (case intermédiaire franchissable,
    /// aucun mur sur les deux arêtes traversées), puis libre au sens physique sur tout le trajet en L,
    /// l'unité restant orientée vers le pas engagé (ARB-A, G1, A2).
    /// </summary>
    private bool PassageIsPracticable(GridPosition from, Direction passage, GridPosition to, Direction heading)
    {
        GridPosition middle = from.Step(passage);
        if (!Map.Contains(middle) || Map.IsBlocked(middle))
        {
            return false;
        }

        Direction secondLeg = DirectionBetween(middle, to);
        if (Map.WallBetween(from, passage) is not null || Map.WallBetween(middle, secondLeg) is not null)
        {
            return false;
        }

        return _geometry.TranslationIsFree(from, middle, heading) && _geometry.TranslationIsFree(middle, to, heading);
    }

    private static Direction DirectionBetween(GridPosition from, GridPosition to) =>
        (to.Column - from.Column, to.Row - from.Row) switch
        {
            (0, -1) => Direction.N,
            (1, 0) => Direction.E,
            (0, 1) => Direction.S,
            (-1, 0) => Direction.W,
            _ => throw new InvalidOperationException($"Les cases {from} et {to} ne sont pas voisines orthogonales."),
        };
}

/// <summary>Contrôles d'un pas indépendants des ressources : refus éventuel, coût réel, rotation, passage.</summary>
internal sealed record StepPlan(StepRefusal Refusal, StepCost? Cost, RotationSense Rotation, Direction? Passage)
{
    public static StepPlan Refused(StepRefusal refusal, StepCost? cost) => new(refusal, cost, RotationSense.None, null);

    public static StepPlan Admitted(StepCost cost, RotationSense rotation, Direction? passage) => new(StepRefusal.None, cost, rotation, passage);
}
