namespace Bastion.Simulation.Movement;

/// <summary>
/// État de l'unité : position, orientation, TU et énergie courantes (A4 f). Immuable : un pas refusé
/// le laisse tel quel (A9). Un état se crée par <see cref="MovementModel.CreateState"/>, qui le valide.
/// </summary>
public sealed record UnitState
{
    internal UnitState(GridPosition position, Direction orientation, int tu, int energy)
    {
        Position = position;
        Orientation = orientation;
        Tu = tu;
        Energy = energy;
    }

    public GridPosition Position { get; init; }

    public Direction Orientation { get; init; }

    public int Tu { get; init; }

    public int Energy { get; init; }
}
