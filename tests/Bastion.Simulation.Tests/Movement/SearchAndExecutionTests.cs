using Bastion.Simulation.Movement;
using static Bastion.Simulation.Tests.Movement.TestWorld;

namespace Bastion.Simulation.Tests.Movement;

/// <summary>Zone atteignable, choix du chemin et exécution : T05 à T09 et T15 à T18 (MEC-0003).</summary>
public class SearchAndExecutionTests
{
    [Fact]
    public void T05_ReachableZoneUsesBothResources()
    {
        MovementModel model = Model(Map(5, 5));

        Reachability plenty = model.ComputeReachability(model.CreateState(At(2, 2), Direction.N, 8, 100));
        GridPosition[] neighbours = [At(1, 1), At(2, 1), At(3, 1), At(1, 2), At(3, 2), At(1, 3), At(2, 3), At(3, 3)];
        GridPosition[] twoStraight = [At(2, 0), At(0, 2), At(4, 2), At(2, 4)];
        Assert.Equal(12, plenty.Zone.Count);
        Assert.True(plenty.Zone.ToHashSet().SetEquals(neighbours.Concat(twoStraight)));

        Reachability lowEnergy = model.ComputeReachability(model.CreateState(At(2, 2), Direction.N, 8, 3));
        Assert.True(lowEnergy.Zone.ToHashSet().SetEquals(neighbours));
    }

    [Fact]
    public void T06_OrderOutsideTheZoneIsRefusedWithoutDebitOrMove()
    {
        MovementModel model = Model(Map(5, 5));
        UnitState start = model.CreateState(At(2, 2), Direction.N, 8, 100);

        OrderOutcome outcome = model.ExecuteOrder(start, At(4, 4));

        Assert.False(outcome.InZone);
        Assert.Null(outcome.Execution);
        Assert.Same(start, outcome.FinalState);
    }

    [Fact]
    public void T07_EnergyBreaksATieInTu()
    {
        var plusQuarter = new TerrainType("configuré +25 %", 1.25m);
        MovementModel model = Model(Map(3, 2).SetTerrain(At(1, 0), plusQuarter).SetTerrain(At(1, 1), plusQuarter));

        Reachability reachability = model.ComputeReachability(model.CreateState(At(0, 1), Direction.N, 60, 100));

        Assert.True(reachability.TryGetPath(At(2, 0), out PlannedPath? path));
        Assert.Equal([Direction.E, Direction.NE], path.Steps);
        Assert.Equal(11, path.Tu);
        Assert.Equal(6, path.Energy);
    }

    [Fact]
    public void T08_CheaperTuPathIsNotAdmissibleWithoutEnoughEnergy()
    {
        MovementModel model = Model(Map(2, 2), rules: new MovementRules(4, 2, 3m));

        Reachability low = model.ComputeReachability(model.CreateState(At(0, 1), Direction.N, 60, 5));
        Assert.True(low.TryGetPath(At(1, 0), out PlannedPath? lowPath));
        Assert.Equal([Direction.N, Direction.E], lowPath.Steps);
        Assert.Equal((8, 4), (lowPath.Tu, lowPath.Energy));

        Reachability enough = model.ComputeReachability(model.CreateState(At(0, 1), Direction.N, 60, 6));
        Assert.True(enough.TryGetPath(At(1, 0), out PlannedPath? enoughPath));
        Assert.Equal([Direction.NE], enoughPath.Steps);
        Assert.Equal((6, 6), (enoughPath.Tu, enoughPath.Energy));
    }

    [Fact]
    public void T09_DirectionOrderBreaksAFullTie()
    {
        MovementModel model = Model(Map(3, 2));

        Reachability reachability = model.ComputeReachability(model.CreateState(At(0, 1), Direction.N, 60, 100));

        Assert.True(reachability.TryGetPath(At(2, 0), out PlannedPath? path));
        Assert.Equal([Direction.NE, Direction.E], path.Steps);
        Assert.Equal((10, 5), (path.Tu, path.Energy));
    }

    [Fact]
    public void T15_ExecutionOfAThreeStepPath()
    {
        MovementModel model = Model(Map(5, 5));
        UnitState start = model.CreateState(At(0, 4), Direction.N, 60, 100);

        PathOutcome outcome = model.ExecutePath(start, [Direction.N, Direction.NE, Direction.E]);

        Assert.True(outcome.Completed);
        Assert.Equal(At(2, 2), outcome.FinalState.Position);
        Assert.Equal(Direction.E, outcome.FinalState.Orientation);
        Assert.Equal(60 - (4 + 6 + 4), outcome.FinalState.Tu);
        Assert.Equal(100 - (2 + 3 + 2), outcome.FinalState.Energy);
    }

    [Fact]
    public void T16_CostIncreasedButPayableIsDebitedAtItsRealCost()
    {
        (UnitState start, PlannedPath path) = PlanEastEast();
        MovementModel changed = Model(Map(3, 2).SetTerrain(At(2, 1), TerrainType.Difficult));

        PathOutcome outcome = changed.ExecutePath(start, path.Steps);

        Assert.True(outcome.Completed);
        Assert.Equal(new StepCost(6, 3), outcome.Steps[1].Cost);
        Assert.Equal(At(2, 1), outcome.FinalState.Position);
        Assert.Equal(0, outcome.FinalState.Tu);
        Assert.Equal(95, outcome.FinalState.Energy);
    }

    [Fact]
    public void T17_StepThatBecameUnpayableIsRefusedAndTheStateIsKept()
    {
        (UnitState start, PlannedPath path) = PlanEastEast();
        MovementModel changed = Model(Map(3, 2).SetTerrain(At(2, 1), TerrainType.VeryDifficult));

        PathOutcome outcome = changed.ExecutePath(start, path.Steps);

        Assert.False(outcome.Completed);
        Assert.Equal(2, outcome.Steps.Count);
        Assert.True(outcome.Steps[0].Accepted);
        Assert.Equal(StepRefusal.InsufficientTu, outcome.Steps[1].Refusal);
        Assert.Equal(new StepCost(8, 4), outcome.Steps[1].Cost);
        Assert.Equal(At(1, 1), outcome.FinalState.Position);
        Assert.Equal(Direction.E, outcome.FinalState.Orientation);
        Assert.Equal(6, outcome.FinalState.Tu);
        Assert.Equal(98, outcome.FinalState.Energy);
    }

    [Fact]
    public void T18_SameMapAndStateGiveTheSameZonePathPassageAndRotation()
    {
        MovementModel first = Model(Map(5, 5).AddWall(At(2, 2), Direction.N, WallType.Standard));
        MovementModel second = Model(Map(5, 5).AddWall(At(2, 2), Direction.N, WallType.Standard));
        UnitState start = first.CreateState(At(2, 2), Direction.W, 30, 100);

        Reachability a = first.ComputeReachability(start);
        Reachability b = second.ComputeReachability(start);
        Assert.True(a.Zone.ToHashSet().SetEquals(b.Zone));
        foreach (GridPosition cell in a.Zone)
        {
            Assert.True(a.TryGetPath(cell, out PlannedPath? pathA));
            Assert.True(b.TryGetPath(cell, out PlannedPath? pathB));
            Assert.Equal(pathA.Steps, pathB.Steps);
        }

        StepOutcome stepA = first.EvaluateStep(start, Direction.NE);
        StepOutcome stepB = second.EvaluateStep(start, Direction.NE);
        Assert.Equal((stepA.Refusal, stepA.Passage, stepA.Rotation), (stepB.Refusal, stepB.Passage, stepB.Rotation));
        Assert.Equal(Direction.E, stepA.Passage);
        Assert.Equal(RotationSense.Clockwise, stepA.Rotation);
    }

    [Fact]
    public void ZoneAndPathComputationsDoNotModifyTheUnitStateOrTheMap()
    {
        MovementModel model = Model(Map(4, 4).SetTerrain(At(1, 1), TerrainType.Difficult));
        UnitState start = model.CreateState(At(0, 0), Direction.S, 20, 10);
        UnitState copy = start with { };

        Reachability reachability = model.ComputeReachability(start);
        model.EvaluateStep(start, Direction.SE);

        Assert.NotEmpty(reachability.Zone);
        Assert.Equal(copy, start);
        Assert.Equal(TerrainType.Difficult, model.Map.TerrainAt(At(1, 1)));
    }

    /// <summary>
    /// Avenant n° 2, RL-03 (hors registre) : l'ordre s'arrête au premier pas refusé, sans exécuter les pas suivants,
    /// sans nouveau calcul de chemin, et les effets des pas déjà exécutés sont conservés (Q3.4, Q4.21, A9).
    /// Carte de 3 × 4 ; unité de 600 × 600 mm orientée N en (0,3), avec 60 TU et 100 d'énergie ; chemin calculé
    /// vers (1,0) : [N, N, NE]. Avant l'exécution, la case (0,1) devient infranchissable (A4 g) : le 2e pas est
    /// refusé. Le 3e pas, NE depuis (0,2), resterait exécutable, et (1,0) resterait atteignable par un autre chemin.
    /// </summary>
    [Fact]
    public void RL03_OrderStopsAtTheFirstRefusedStep()
    {
        MovementModel planned = Model(Map(3, 4));
        UnitState start = planned.CreateState(At(0, 3), Direction.N, 60, 100);
        Assert.True(planned.ComputeReachability(start).TryGetPath(At(1, 0), out PlannedPath? path));
        Assert.Equal([Direction.N, Direction.N, Direction.NE], path.Steps);
        MovementModel changed = Model(Map(3, 4).Block(At(0, 1)));

        PathOutcome outcome = changed.ExecutePath(start, path.Steps);

        Assert.False(outcome.Completed);
        Assert.Equal(2, outcome.Steps.Count);
        Assert.True(outcome.Steps[0].Accepted);
        Assert.Equal(StepRefusal.ArrivalBlocked, outcome.Steps[1].Refusal);
        Assert.Same(outcome.Steps[0].State, outcome.FinalState);
        Assert.Equal(At(0, 2), outcome.FinalState.Position);
        Assert.Equal(Direction.N, outcome.FinalState.Orientation);
        Assert.Equal((56, 98), (outcome.FinalState.Tu, outcome.FinalState.Energy)); // seul le 1er pas est débité

        // Le 3e pas aurait été exécutable, et un nouveau calcul aurait trouvé un chemin : rien de tel n'a eu lieu.
        Assert.True(changed.EvaluateStep(outcome.FinalState, Direction.NE).Accepted);
        Assert.True(changed.ComputeReachability(outcome.FinalState).Contains(At(1, 0)));
    }

    /// <summary>Carte de 3 × 2, unité de 600 × 600 orientée N en (0,1), 10 TU et 100 d'énergie ; chemin vers (2,1).</summary>
    private static (UnitState Start, PlannedPath Path) PlanEastEast()
    {
        MovementModel normal = Model(Map(3, 2));
        UnitState start = normal.CreateState(At(0, 1), Direction.N, 10, 100);
        Assert.True(normal.ComputeReachability(start).TryGetPath(At(2, 1), out PlannedPath? path));
        Assert.Equal([Direction.E, Direction.E], path.Steps);
        return (start, path);
    }
}
