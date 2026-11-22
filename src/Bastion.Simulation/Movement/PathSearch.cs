using System.Diagnostics.CodeAnalysis;

namespace Bastion.Simulation.Movement;

/// <summary>
/// Zone atteignable (Z1, G3) et meilleur chemin vers chacune de ses cases (G4, Q4.16) : TU minimales,
/// puis énergie minimale, puis ordre lexicographique des suites de directions N, NE, E, SE, S, SW, W, NW.
/// La case de départ n'en fait pas partie.
/// </summary>
public sealed class Reachability
{
    private readonly Dictionary<GridPosition, PlannedPath> _paths;

    internal Reachability(Dictionary<GridPosition, PlannedPath> paths)
    {
        _paths = paths;
    }

    /// <summary>Cases de la zone atteignable.</summary>
    public IReadOnlyCollection<GridPosition> Zone => _paths.Keys;

    public bool Contains(GridPosition cell) => _paths.ContainsKey(cell);

    public bool TryGetPath(GridPosition destination, [NotNullWhen(true)] out PlannedPath? path) =>
        _paths.TryGetValue(destination, out path);
}

/// <summary>
/// Recherche « meilleur d'abord » sur les états (case, orientation) : l'orientation compte, car elle
/// conditionne le contrôle des rotations. Les étiquettes sont traitées dans l'ordre (TU, énergie,
/// suite de directions) ; une étiquette dominée en TU et en énergie dans le même état est écartée.
/// La recherche termine, car chaque pas coûte au moins 1 TU (A4 d) et les ressources sont bornées.
/// </summary>
internal static class PathSearch
{
    public static Reachability Run(MovementModel model, UnitState start)
    {
        var queue = new PriorityQueue<Label, Label>(LabelOrder.Instance);
        var settled = new Dictionary<(GridPosition, Direction), List<(int Tu, int Energy)>>();
        var best = new Dictionary<GridPosition, PlannedPath>();
        var origin = new Label(start.Position, start.Orientation, 0, 0, []);
        queue.Enqueue(origin, origin);
        while (queue.TryDequeue(out Label? label, out _))
        {
            var state = (label.Cell, label.Orientation);
            if (!settled.TryGetValue(state, out List<(int Tu, int Energy)>? front))
            {
                front = [];
                settled[state] = front;
            }

            if (front.Any(other => other.Tu <= label.Tu && other.Energy <= label.Energy))
            {
                continue;
            }

            front.Add((label.Tu, label.Energy));
            if (label.Steps.Length > 0 && !best.ContainsKey(label.Cell))
            {
                best[label.Cell] = new PlannedPath(label.Steps, label.Tu, label.Energy);
            }

            foreach (Direction direction in Enum.GetValues<Direction>())
            {
                StepPlan plan = model.PlanStep(label.Cell, label.Orientation, direction);
                if (plan.Refusal != StepRefusal.None)
                {
                    continue;
                }

                StepCost cost = plan.Cost!.Value;
                int tu = label.Tu + cost.Tu;
                int energy = label.Energy + cost.Energy;
                if (tu > start.Tu || energy > start.Energy)
                {
                    continue;
                }

                var next = new Label(label.Cell.Step(direction), direction, tu, energy, [.. label.Steps, direction]);
                queue.Enqueue(next, next);
            }
        }

        best.Remove(start.Position);
        return new Reachability(best);
    }

    private sealed record Label(GridPosition Cell, Direction Orientation, int Tu, int Energy, Direction[] Steps);

    private sealed class LabelOrder : IComparer<Label>
    {
        public static LabelOrder Instance { get; } = new();

        public int Compare(Label? x, Label? y)
        {
            ArgumentNullException.ThrowIfNull(x);
            ArgumentNullException.ThrowIfNull(y);
            int comparison = x.Tu.CompareTo(y.Tu);
            if (comparison != 0)
            {
                return comparison;
            }

            comparison = x.Energy.CompareTo(y.Energy);
            if (comparison != 0)
            {
                return comparison;
            }

            int length = Math.Min(x.Steps.Length, y.Steps.Length);
            for (int index = 0; index < length; index++)
            {
                comparison = ((int)x.Steps[index]).CompareTo((int)y.Steps[index]);
                if (comparison != 0)
                {
                    return comparison;
                }
            }

            return x.Steps.Length.CompareTo(y.Steps.Length);
        }
    }
}
