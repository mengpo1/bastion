namespace Bastion.Simulation.Movement;

/// <summary>Case de la carte : colonne (vers l'est) et ligne (vers le sud).</summary>
public readonly record struct GridPosition(int Column, int Row)
{
    /// <summary>Case voisine dans la direction donnée.</summary>
    public GridPosition Step(Direction direction)
    {
        (int columns, int rows) = direction.Offset();
        return new GridPosition(Column + columns, Row + rows);
    }

    public override string ToString() => $"({Column},{Row})";
}
