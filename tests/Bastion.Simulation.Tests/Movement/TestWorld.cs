using Bastion.Simulation.Movement;

namespace Bastion.Simulation.Tests.Movement;

/// <summary>
/// Outils des tests de MEC-0003. Repère des tests : (colonne, ligne), N = ligne − 1, E = colonne + 1.
/// Sauf mention contraire : case de 1 500 mm, mur de 100 mm, unité de 600 × 600 mm.
/// </summary>
internal static class TestWorld
{
    public static GridPosition At(int column, int row) => new(column, row);

    public static TacticalMapBuilder Map(int columns, int rows) => new(columns, rows, 1500m);

    public static MovementModel Model(TacticalMapBuilder map, UnitBody? body = null, MovementRules? rules = null) =>
        new(map.Build(), rules ?? MovementRules.Initial, body ?? UnitBody.StandardHuman);

    /// <summary>Murs à l'ouest et à l'est de toutes les cases d'une colonne : couloir nord-sud.</summary>
    public static TacticalMapBuilder WithNorthSouthCorridor(this TacticalMapBuilder map, int column, int rows)
    {
        for (int row = 0; row < rows; row++)
        {
            map.AddWall(At(column, row), Direction.W, WallType.Standard);
            map.AddWall(At(column, row), Direction.E, WallType.Standard);
        }

        return map;
    }
}
