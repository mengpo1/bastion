using Bastion.Simulation.Movement;
using static Bastion.Simulation.Tests.Movement.TestWorld;

namespace Bastion.Simulation.Tests.Movement;

/// <summary>Coûts en TU et en énergie : T01 à T04 et T03b (MEC-0003).</summary>
public class CostTests
{
    private static readonly MovementRules Rules = MovementRules.Initial;

    [Fact]
    public void T01_OrthogonalStepOnNormalTerrainCosts4TuAnd2Energy()
    {
        Assert.Equal(new StepCost(4, 2), Rules.CostOf(Direction.E, TerrainType.Normal));

        MovementModel model = Model(Map(3, 3));
        UnitState start = model.CreateState(At(1, 1), Direction.E, 60, 100);
        StepOutcome outcome = model.EvaluateStep(start, Direction.E);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(new StepCost(4, 2), outcome.Cost);
        Assert.Equal(56, outcome.State.Tu);
        Assert.Equal(98, outcome.State.Energy);
    }

    [Fact]
    public void T02_DiagonalStepOnNormalTerrainCosts6TuAnd3Energy()
    {
        Assert.Equal(new StepCost(6, 3), Rules.CostOf(Direction.NE, TerrainType.Normal));
    }

    [Fact]
    public void T03_DifficultAndVeryDifficultTerrains()
    {
        Assert.Equal(new StepCost(6, 3), Rules.CostOf(Direction.E, TerrainType.Difficult));
        Assert.Equal(new StepCost(9, 5), Rules.CostOf(Direction.NE, TerrainType.Difficult));
        Assert.Equal(new StepCost(8, 4), Rules.CostOf(Direction.E, TerrainType.VeryDifficult));
        Assert.Equal(new StepCost(12, 6), Rules.CostOf(Direction.NE, TerrainType.VeryDifficult));
    }

    [Fact]
    public void T03b_CommonFactorOf125PercentAndConfiguredDiagonalEnergyMultiplier()
    {
        var configured = new TerrainType("configuré +25 %", 1.25m);

        Assert.Equal(new StepCost(5, 3), Rules.CostOf(Direction.E, configured));
        Assert.Equal(new StepCost(7, 5), Rules.CostOf(Direction.NE, configured));

        var multiplierTwo = new MovementRules(4, 2, 2m);
        Assert.Equal(new StepCost(7, 6), multiplierTwo.CostOf(Direction.NE, configured));
    }

    [Fact]
    public void T04_OnlyTheArrivalTerrainCounts()
    {
        MovementModel model = Model(Map(3, 3).SetTerrain(At(1, 1), TerrainType.Difficult));
        UnitState start = model.CreateState(At(1, 1), Direction.E, 60, 100);

        StepOutcome outcome = model.EvaluateStep(start, Direction.E);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(new StepCost(4, 2), outcome.Cost);
    }
}
