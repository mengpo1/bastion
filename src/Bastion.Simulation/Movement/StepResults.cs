namespace Bastion.Simulation.Movement;

/// <summary>Motif du refus d'un pas.</summary>
public enum StepRefusal
{
    None,

    /// <summary>La case d'arrivée est hors de la carte.</summary>
    OutsideMap,

    /// <summary>La case d'arrivée est infranchissable.</summary>
    ArrivalBlocked,

    /// <summary>La rotation vers le pas chevaucherait un obstacle, dans les deux sens pour un demi-tour (A5, A7).</summary>
    RotationBlocked,

    /// <summary>Un mur occupe l'arête traversée par le pas orthogonal (N1, Q3.12).</summary>
    WallOnEdge,

    /// <summary>Le volume balayé pendant le pas orthogonal chevaucherait un obstacle (A2).</summary>
    VolumeCollision,

    /// <summary>Aucun des deux passages du pas diagonal n'est praticable (S3, N2, ARB-A, G1, A2).</summary>
    NoPracticablePassage,

    /// <summary>Les TU restantes ne couvrent pas le coût réel du pas (G3).</summary>
    InsufficientTu,

    /// <summary>L'énergie restante ne couvre pas le coût réel du pas (G3).</summary>
    InsufficientEnergy,
}

/// <summary>Sens de la rotation effectuée avant un pas.</summary>
public enum RotationSense
{
    None,
    Clockwise,
    CounterClockwise,
}

/// <summary>Choix du sens de rotation (A5, A7).</summary>
public static class RotationRules
{
    /// <summary>Écart d'orientation, en huitièmes de tour comptés dans le sens horaire (0 à 7).</summary>
    public static int ClockwiseEighths(Direction from, Direction to) => ((int)to - (int)from + 8) % 8;

    /// <summary>
    /// Sens d'un demi-tour (A7) : « Priorité au sens horaire. Si ce sens est physiquement bloqué,
    /// essayer le sens antihoraire. Refuser le pas uniquement lorsque les deux sens sont impraticables. »
    /// Rend <c>null</c> si les deux sens sont bloqués.
    /// </summary>
    public static RotationSense? ChooseHalfTurn(bool clockwiseFree, bool counterClockwiseFree)
    {
        if (clockwiseFree)
        {
            return RotationSense.Clockwise;
        }

        return counterClockwiseFree ? RotationSense.CounterClockwise : null;
    }
}

/// <summary>
/// Résultat de l'évaluation d'un pas. Si le pas est refusé, <see cref="State"/> est l'état initial,
/// inchangé (A9).
/// </summary>
public sealed record StepOutcome(
    Direction Direction,
    StepRefusal Refusal,
    StepCost? Cost,
    RotationSense Rotation,
    Direction? Passage,
    UnitState State)
{
    public bool Accepted => Refusal == StepRefusal.None;

    /// <summary>Description lisible du résultat.</summary>
    public string Message => Refusal switch
    {
        StepRefusal.None => $"Pas {Direction} exécuté vers {State.Position}.",
        StepRefusal.OutsideMap => $"Pas {Direction} refusé : la case d'arrivée est hors de la carte.",
        StepRefusal.ArrivalBlocked => $"Pas {Direction} refusé : la case d'arrivée est infranchissable.",
        StepRefusal.RotationBlocked => $"Pas {Direction} refusé : la rotation vers {Direction} chevaucherait un obstacle.",
        StepRefusal.WallOnEdge => $"Pas {Direction} refusé : un mur occupe l'arête à traverser.",
        StepRefusal.VolumeCollision => $"Pas {Direction} refusé : le volume de l'unité chevaucherait un obstacle pendant le pas.",
        StepRefusal.NoPracticablePassage => $"Pas {Direction} refusé : aucun des deux passages orthogonaux n'est praticable.",
        StepRefusal.InsufficientTu => $"Pas {Direction} refusé : TU insuffisantes ({Cost?.Tu} requises, {State.Tu} disponibles).",
        StepRefusal.InsufficientEnergy => $"Pas {Direction} refusé : énergie insuffisante ({Cost?.Energy} requise, {State.Energy} disponible).",
        _ => $"Pas {Direction} refusé.",
    };
}

/// <summary>Chemin choisi selon G4 et Q4.16, avec son coût total.</summary>
public sealed record PlannedPath(IReadOnlyList<Direction> Steps, int Tu, int Energy);

/// <summary>Résultat de l'exécution d'un chemin, pas à pas.</summary>
public sealed record PathOutcome(UnitState FinalState, IReadOnlyList<StepOutcome> Steps)
{
    /// <summary>Vrai si tous les pas ont été exécutés.</summary>
    public bool Completed => Steps.All(step => step.Accepted);

    /// <summary>Le pas refusé qui a arrêté l'ordre, s'il y en a un.</summary>
    public StepOutcome? Refused => Steps.FirstOrDefault(step => !step.Accepted);
}

/// <summary>Résultat d'un ordre de déplacement vers une destination.</summary>
public sealed record OrderOutcome(GridPosition Destination, PlannedPath? Path, PathOutcome? Execution, UnitState FinalState)
{
    /// <summary>Vrai si la destination appartenait à la zone atteignable (Z1).</summary>
    public bool InZone => Path is not null;

    public string Message => InZone
        ? Execution!.Completed ? $"Destination {Destination} atteinte." : Execution.Refused!.Message
        : $"Ordre refusé : la destination {Destination} n'appartient pas à la zone atteignable.";
}
