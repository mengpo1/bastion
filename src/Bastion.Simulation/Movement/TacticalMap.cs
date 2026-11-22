namespace Bastion.Simulation.Movement;

/// <summary>
/// Carte tactique de MEC-0003 : un seul niveau, terrain plat et sol stable partout. Elle comporte des
/// cases de largeur uniforme, paire, en millimètres (Q1.1), un terrain par case, des cases entièrement
/// infranchissables et des murs placés sur les arêtes entre les cases. Immuable ; se construit avec
/// <see cref="TacticalMapBuilder"/>.
/// </summary>
public sealed class TacticalMap
{
    private readonly TerrainType[,] _terrain;
    private readonly bool[,] _blocked;
    private readonly Dictionary<WallEdge, WallType> _walls;

    internal TacticalMap(int columns, int rows, int cellWidthMm, TerrainType[,] terrain, bool[,] blocked, Dictionary<WallEdge, WallType> walls)
    {
        Columns = columns;
        Rows = rows;
        CellWidthMm = cellWidthMm;
        _terrain = terrain;
        _blocked = blocked;
        _walls = walls;
    }

    public int Columns { get; }

    public int Rows { get; }

    public int CellWidthMm { get; }

    internal IEnumerable<KeyValuePair<WallEdge, WallType>> Walls => _walls;

    public bool Contains(GridPosition cell) =>
        cell.Column >= 0 && cell.Column < Columns && cell.Row >= 0 && cell.Row < Rows;

    public TerrainType TerrainAt(GridPosition cell)
    {
        RequireInside(cell);
        return _terrain[cell.Column, cell.Row];
    }

    public bool IsBlocked(GridPosition cell)
    {
        RequireInside(cell);
        return _blocked[cell.Column, cell.Row];
    }

    /// <summary>Mur sur l'arête entre deux cases voisines orthogonales, ou <c>null</c>.</summary>
    public WallType? WallBetween(GridPosition cell, Direction side) =>
        _walls.TryGetValue(WallEdge.Of(cell, side), out WallType? wall) ? wall : null;

    private void RequireInside(GridPosition cell)
    {
        if (!Contains(cell))
        {
            throw new ArgumentOutOfRangeException(nameof(cell), cell, $"La case {cell} est hors de la carte ({Columns} × {Rows}).");
        }
    }
}

/// <summary>Arête entre deux cases, rangée comme l'arête est ou sud de sa case ouest ou nord.</summary>
internal readonly record struct WallEdge(GridPosition Cell, bool IsEastEdge)
{
    public static WallEdge Of(GridPosition cell, Direction side) => side switch
    {
        Direction.E => new WallEdge(cell, true),
        Direction.W => new WallEdge(cell.Step(Direction.W), true),
        Direction.S => new WallEdge(cell, false),
        Direction.N => new WallEdge(cell.Step(Direction.N), false),
        _ => throw new ArgumentOutOfRangeException(nameof(side), side, "Un mur se place sur une arête : côté N, E, S ou W."),
    };
}

/// <summary>Construction d'une <see cref="TacticalMap"/>, avec validation des paramètres.</summary>
public sealed class TacticalMapBuilder
{
    private readonly int _columns;
    private readonly int _rows;
    private readonly int _cellWidthMm;
    private readonly TerrainType[,] _terrain;
    private readonly bool[,] _blocked;
    private readonly Dictionary<WallEdge, WallType> _walls = new();

    public TacticalMapBuilder(int columns, int rows, decimal cellWidthMm)
    {
        if (columns < 1 || rows < 1)
        {
            throw new ArgumentOutOfRangeException(nameof(columns), $"La carte doit compter au moins une colonne et une ligne ; reçu : {columns} × {rows}.");
        }

        _cellWidthMm = Millimetres.RequirePositiveInteger(cellWidthMm, "La largeur de case", nameof(cellWidthMm));
        if (_cellWidthMm % 2 != 0)
        {
            throw new ArgumentException(
                $"La largeur de case doit être paire en millimètres (Q1.1) ; valeur reçue : {_cellWidthMm} mm.",
                nameof(cellWidthMm));
        }

        _columns = columns;
        _rows = rows;
        _terrain = new TerrainType[columns, rows];
        _blocked = new bool[columns, rows];
        for (int column = 0; column < columns; column++)
        {
            for (int row = 0; row < rows; row++)
            {
                _terrain[column, row] = TerrainType.Normal;
            }
        }
    }

    public TacticalMapBuilder SetTerrain(GridPosition cell, TerrainType terrain)
    {
        ArgumentNullException.ThrowIfNull(terrain);
        RequireInside(cell);
        _terrain[cell.Column, cell.Row] = terrain;
        return this;
    }

    public TacticalMapBuilder Block(GridPosition cell)
    {
        RequireInside(cell);
        _blocked[cell.Column, cell.Row] = true;
        return this;
    }

    /// <summary>Place un mur sur l'arête entre <paramref name="cell"/> et sa voisine du côté <paramref name="side"/>.</summary>
    public TacticalMapBuilder AddWall(GridPosition cell, Direction side, WallType wall)
    {
        ArgumentNullException.ThrowIfNull(wall);
        RequireInside(cell);
        if (side.IsDiagonal())
        {
            throw new ArgumentException($"Un mur se place sur une arête : côté N, E, S ou W ; reçu : {side}.", nameof(side));
        }

        if (!Inside(cell.Step(side)))
        {
            throw new ArgumentException(
                $"Un mur se place sur une arête entre deux cases ; la case {cell} n'a pas de voisine du côté {side}.",
                nameof(side));
        }

        _walls[WallEdge.Of(cell, side)] = wall;
        return this;
    }

    public TacticalMap Build() =>
        new(_columns, _rows, _cellWidthMm, (TerrainType[,])_terrain.Clone(), (bool[,])_blocked.Clone(), new Dictionary<WallEdge, WallType>(_walls));

    private bool Inside(GridPosition cell) =>
        cell.Column >= 0 && cell.Column < _columns && cell.Row >= 0 && cell.Row < _rows;

    private void RequireInside(GridPosition cell)
    {
        if (!Inside(cell))
        {
            throw new ArgumentOutOfRangeException(nameof(cell), cell, $"La case {cell} est hors de la carte ({_columns} × {_rows}).");
        }
    }
}
