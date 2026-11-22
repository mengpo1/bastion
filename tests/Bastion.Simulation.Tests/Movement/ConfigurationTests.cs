using Bastion.Simulation.Movement;
using static Bastion.Simulation.Tests.Movement.TestWorld;

namespace Bastion.Simulation.Tests.Movement;

/// <summary>Configurations invalides : T19 (MEC-0003).</summary>
public class ConfigurationTests
{
    [Fact]
    public void T19_OddCellWidthIsRefused()
    {
        var error = Assert.Throws<ArgumentException>(() => new TacticalMapBuilder(3, 3, 1501m));
        Assert.Contains("paire", error.Message);
    }

    [Fact]
    public void T19_NonIntegerDimensionIsRefused()
    {
        var error = Assert.Throws<ArgumentException>(() => new UnitBody(600.5m, 600m, 1800m));
        Assert.Contains("entier", error.Message);

        var wallError = Assert.Throws<ArgumentException>(() => new WallType("fin", 99.5m));
        Assert.Contains("entier", wallError.Message);
    }

    [Fact]
    public void T19_ConfigurationAllowingAStepAtZeroTuIsRefused()
    {
        var baseError = Assert.Throws<ArgumentOutOfRangeException>(() => new MovementRules(0, 2, 1.5m));
        Assert.Contains("0 TU", baseError.Message);

        var factorError = Assert.Throws<ArgumentOutOfRangeException>(() => new TerrainType("nul", 0m));
        Assert.Contains("0 TU", factorError.Message);
    }

    [Fact]
    public void T19_OverlappingInitialPositionIsRefused()
    {
        MovementModel model = Model(Map(5, 5).Block(At(3, 2)), new UnitBody(1600m, 1600m, 1800m));

        var error = Assert.Throws<ArgumentException>(() => model.CreateState(At(2, 2), Direction.N, 60, 100));
        Assert.Contains("chevauche", error.Message);
    }
}
