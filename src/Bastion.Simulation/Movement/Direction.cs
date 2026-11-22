namespace Bastion.Simulation.Movement;

/// <summary>
/// Les huit directions de pas (S1), dans l'ordre du départage des chemins de Q4.16 :
/// N, NE, E, SE, S, SW, W, NW. L'ordre des valeurs est significatif.
/// Repère des cases : colonne vers l'est, ligne vers le sud (le nord est la ligne − 1).
/// Une orientation est l'une de ces directions ; leurs valeurs croissent dans le sens horaire.
/// </summary>
public enum Direction
{
    N = 0,
    NE = 1,
    E = 2,
    SE = 3,
    S = 4,
    SW = 5,
    W = 6,
    NW = 7,
}

/// <summary>Propriétés des directions.</summary>
public static class DirectionExtensions
{
    /// <summary>Décalage en colonnes et en lignes d'un pas dans cette direction.</summary>
    public static (int Columns, int Rows) Offset(this Direction direction) => direction switch
    {
        Direction.N => (0, -1),
        Direction.NE => (1, -1),
        Direction.E => (1, 0),
        Direction.SE => (1, 1),
        Direction.S => (0, 1),
        Direction.SW => (-1, 1),
        Direction.W => (-1, 0),
        Direction.NW => (-1, -1),
        _ => throw new ArgumentOutOfRangeException(nameof(direction), direction, "Direction inconnue."),
    };

    public static bool IsDiagonal(this Direction direction) => ((int)direction & 1) == 1;

    /// <summary>
    /// Les deux passages orthogonaux d'un pas diagonal, dans l'ordre de priorité N, E, S, W (A3) :
    /// NE et NW passent d'abord par N, SE par E, SW par S.
    /// </summary>
    public static (Direction First, Direction Second) Passages(this Direction diagonal) => diagonal switch
    {
        Direction.NE => (Direction.N, Direction.E),
        Direction.SE => (Direction.E, Direction.S),
        Direction.SW => (Direction.S, Direction.W),
        Direction.NW => (Direction.N, Direction.W),
        _ => throw new ArgumentOutOfRangeException(nameof(diagonal), diagonal, "Seul un pas diagonal a deux passages."),
    };
}
