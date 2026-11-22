using Bastion.Simulation.Movement;
using static Bastion.Simulation.Tests.Movement.TestWorld;

namespace Bastion.Simulation.Tests.Movement;

/// <summary>Géométrie, passages, rotations et collisions : T10 à T14 et T20 à T29 (MEC-0003).</summary>
public class GeometryTests
{
    private static readonly UnitBody Wide1400x600 = new(1400m, 600m, 1800m);
    private static readonly UnitBody Square1600 = new(1600m, 1600m, 1800m);
    private static readonly UnitBody Square1300 = new(1300m, 1300m, 1800m);
    private static readonly UnitBody Wide1400x200 = new(1400m, 200m, 1800m);
    private static readonly UnitBody Deep200x1400 = new(200m, 1400m, 1800m);
    private static readonly UnitBody Wide1700x600 = new(1700m, 600m, 1800m);
    private static readonly UnitBody Square1200 = new(1200m, 1200m, 1800m);

    [Fact]
    public void T10_DiagonalRefusedWhenBothPassagesAreWalled_ThenAdmittedThroughTheOpenOne()
    {
        MovementModel walled = Model(Map(3, 3)
            .AddWall(At(1, 1), Direction.N, WallType.Standard)
            .AddWall(At(1, 1), Direction.E, WallType.Standard));
        StepOutcome refused = walled.EvaluateStep(walled.CreateState(At(1, 1), Direction.N, 60, 100), Direction.NE);
        Assert.Equal(StepRefusal.NoPracticablePassage, refused.Refusal);

        MovementModel northOnly = Model(Map(3, 3).AddWall(At(1, 1), Direction.N, WallType.Standard));
        StepOutcome admitted = northOnly.EvaluateStep(northOnly.CreateState(At(1, 1), Direction.N, 60, 100), Direction.NE);
        Assert.True(admitted.Accepted, admitted.Message);
        Assert.Equal(Direction.E, admitted.Passage);
        Assert.Equal(new StepCost(6, 3), admitted.Cost);
        Assert.Equal(At(2, 0), admitted.State.Position);
    }

    [Fact]
    public void T11_DiagonalRefusedWhenNoPassageIsPracticable()
    {
        MovementModel model = Model(Map(3, 3)
            .Block(At(1, 0))
            .AddWall(At(2, 1), Direction.N, WallType.Standard));

        StepOutcome outcome = model.EvaluateStep(model.CreateState(At(1, 1), Direction.N, 60, 100), Direction.NE);

        Assert.Equal(StepRefusal.NoPracticablePassage, outcome.Refusal);
    }

    [Fact]
    public void T12_ContactWithBothCorridorWallsIsAllowed()
    {
        MovementModel model = Model(Map(3, 3).WithNorthSouthCorridor(1, 3), Wide1400x600);

        UnitState start = model.CreateState(At(1, 1), Direction.N, 60, 100);
        StepOutcome outcome = model.EvaluateStep(start, Direction.N);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(At(1, 0), outcome.State.Position);
    }

    [Fact]
    public void T12_CounterCheck_TwoMoreMillimetresIsAnOverlap()
    {
        MovementModel model = Model(Map(3, 3).WithNorthSouthCorridor(1, 3), new UnitBody(1402m, 600m, 1800m));

        Assert.Throws<ArgumentException>(() => model.CreateState(At(1, 1), Direction.N, 60, 100));
    }

    [Fact]
    public void T13_VolumeMayExceedItsCellButMayNotOverlapAnImpassableCell()
    {
        MovementModel model = Model(Map(5, 6).Block(At(3, 1)), Square1600);
        UnitState start = model.CreateState(At(2, 4), Direction.N, 60, 100);

        StepOutcome first = model.EvaluateStep(start, Direction.N);
        Assert.True(first.Accepted, first.Message);
        Assert.Equal(At(2, 3), first.State.Position);

        StepOutcome second = model.EvaluateStep(first.State, Direction.N);
        Assert.Equal(StepRefusal.VolumeCollision, second.Refusal);
        Assert.Same(first.State, second.State);
        Assert.Equal(At(2, 3), second.State.Position);
        Assert.Equal(Direction.N, second.State.Orientation);
        Assert.Equal(60 - 4, second.State.Tu);
        Assert.Equal(100 - 2, second.State.Energy);
    }

    [Fact]
    public void T13_TargetCellRemainsInTheReachableZoneAndIsReachedFacingNorthWest()
    {
        MovementModel model = Model(Map(5, 6).Block(At(3, 1)), Square1600);
        UnitState start = model.CreateState(At(2, 4), Direction.N, 60, 100);

        // La zone atteignable est calculée depuis l'état initial en (2,4), avec 60 TU et 100 d'énergie,
        // et non depuis (2,3), où se trouve l'unité après le 1er pas N.
        Reachability reachability = model.ComputeReachability(start);

        Assert.Contains(At(2, 2), reachability.Zone);
        Assert.True(reachability.TryGetPath(At(2, 2), out PlannedPath? path));
        Assert.Equal([Direction.NE, Direction.NW], path.Steps);
        Assert.Equal((12, 6), (path.Tu, path.Energy));

        PathOutcome execution = model.ExecutePath(start, path.Steps);
        Assert.True(execution.Completed);
        Assert.Equal(Direction.N, execution.Steps[0].Passage);
        Assert.Equal(Direction.W, execution.Steps[1].Passage);
        Assert.Equal(At(2, 2), execution.FinalState.Position);
        Assert.Equal(Direction.NW, execution.FinalState.Orientation);
        Assert.Equal((48, 94), (execution.FinalState.Tu, execution.FinalState.Energy)); // 60 − 12 TU, 100 − 6 d'énergie
    }

    [Fact]
    public void T14_InACorridorAStepRequiringARotationIsRefused()
    {
        MovementModel model = Model(Map(3, 3).WithNorthSouthCorridor(1, 3), Square1300);
        UnitState start = model.CreateState(At(1, 1), Direction.N, 60, 100);

        Assert.True(model.EvaluateStep(start, Direction.N).Accepted);
        Assert.Equal(StepRefusal.RotationBlocked, model.EvaluateStep(start, Direction.NE).Refusal);
        Assert.Equal(StepRefusal.RotationBlocked, model.EvaluateStep(start, Direction.S).Refusal);
    }

    [Theory]
    [InlineData(Direction.NE, Direction.N)]
    [InlineData(Direction.SE, Direction.E)]
    [InlineData(Direction.SW, Direction.S)]
    [InlineData(Direction.NW, Direction.N)]
    public void T20_T21_T22_PassagePriorityNorthEastSouthWest(Direction diagonal, Direction expectedPassage)
    {
        MovementModel model = Model(Map(3, 3));

        StepOutcome outcome = model.EvaluateStep(model.CreateState(At(1, 1), Direction.N, 60, 100), diagonal);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(expectedPassage, outcome.Passage);
    }

    [Fact]
    public void T23_PassageNorthCrossedByAWall_PassageEastIsUsed()
    {
        MovementModel model = Model(Map(3, 3).AddWall(At(1, 0), Direction.E, WallType.Standard));

        StepOutcome outcome = model.EvaluateStep(model.CreateState(At(1, 1), Direction.N, 60, 100), Direction.NE);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(Direction.E, outcome.Passage);
    }

    [Fact]
    public void T24_StepThroughAWallIsRefusedAndNoRotationIsApplied()
    {
        MovementModel model = Model(Map(3, 3).AddWall(At(1, 1), Direction.E, WallType.Standard));
        UnitState start = model.CreateState(At(1, 1), Direction.N, 60, 100);

        StepOutcome outcome = model.EvaluateStep(start, Direction.E);

        Assert.Equal(StepRefusal.WallOnEdge, outcome.Refusal);
        Assert.Same(start, outcome.State);
        Assert.Equal(At(1, 1), outcome.State.Position);
        Assert.Equal(Direction.N, outcome.State.Orientation);
        Assert.Equal(60, outcome.State.Tu);
        Assert.Equal(100, outcome.State.Energy);
    }

    [Fact]
    public void T25_RealRectangleRotatesUnderTheNorthWall_ThenPassesEast()
    {
        MovementModel model = Model(Map(3, 3).AddWall(At(1, 1), Direction.N, WallType.Standard), Wide1400x200);

        StepOutcome outcome = model.EvaluateStep(model.CreateState(At(1, 1), Direction.N, 60, 100), Direction.NE);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(RotationSense.Clockwise, outcome.Rotation);
        Assert.Equal(Direction.E, outcome.Passage);
        Assert.Equal(At(2, 0), outcome.State.Position);
        Assert.Equal(Direction.NE, outcome.State.Orientation);
    }

    [Fact]
    public void T26_RealRectangleRotatesBesideTheEastWall_ThenPassesNorth()
    {
        MovementModel model = Model(Map(3, 3).AddWall(At(1, 1), Direction.E, WallType.Standard), Deep200x1400);

        StepOutcome outcome = model.EvaluateStep(model.CreateState(At(1, 1), Direction.N, 60, 100), Direction.NE);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(RotationSense.Clockwise, outcome.Rotation);
        Assert.Equal(Direction.N, outcome.Passage);
    }

    [Fact]
    public void T27_HalfTurnOnFreeGroundIsClockwise()
    {
        MovementModel model = Model(Map(3, 3));

        StepOutcome outcome = model.EvaluateStep(model.CreateState(At(1, 1), Direction.N, 60, 100), Direction.S);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(RotationSense.Clockwise, outcome.Rotation);
        Assert.Equal(new StepCost(4, 2), outcome.Cost);
        Assert.Equal(Direction.S, outcome.State.Orientation);
    }

    [Fact]
    public void T28_HalfTurnBlockedInBothSensesIsRefusedWithoutAnyChange()
    {
        MovementModel model = Model(Map(3, 3).WithNorthSouthCorridor(1, 3), Wide1400x200);
        UnitState start = model.CreateState(At(1, 1), Direction.N, 60, 100);

        StepOutcome outcome = model.EvaluateStep(start, Direction.S);

        Assert.Equal(StepRefusal.RotationBlocked, outcome.Refusal);
        Assert.Same(start, outcome.State);
        Assert.Equal(At(1, 1), outcome.State.Position);
        Assert.Equal(Direction.N, outcome.State.Orientation);
        Assert.Equal(60, outcome.State.Tu);
        Assert.Equal(100, outcome.State.Energy);
    }

    [Theory]
    [InlineData(true, true, RotationSense.Clockwise)]
    [InlineData(true, false, RotationSense.Clockwise)]
    [InlineData(false, true, RotationSense.CounterClockwise)]
    [InlineData(false, false, null)]
    public void T29_HalfTurnSenseChoice(bool clockwiseFree, bool counterClockwiseFree, RotationSense? expected)
    {
        Assert.Equal(expected, RotationRules.ChooseHalfTurn(clockwiseFree, counterClockwiseFree));
    }

    /// <summary>
    /// Avenant n° 2, RL-01 (hors registre) : le volume est contrôlé pendant toute la translation, pas seulement
    /// à ses extrémités (A2). Unité de 1 700 × 600 mm (largeur 1 700, profondeur 600), orientée E en (1,1) ;
    /// mur sur l'arête est de (1,0). L'emprise s'étend à 850 mm au nord du centre, soit 100 mm au-delà de
    /// l'extrémité sud du mur, située à 750 mm. Au départ, elle s'arrête à 400 mm de la face ouest du mur ;
    /// à l'arrivée en (2,1), à 400 mm de sa face est. Seul le volume balayé pendant le pas E chevauche le mur.
    /// </summary>
    [Fact]
    public void RL01_VolumeIsCheckedDuringTheWholeTranslation()
    {
        MovementModel model = Model(Map(3, 3).AddWall(At(1, 0), Direction.E, WallType.Standard), Wide1700x600);
        UnitState start = model.CreateState(At(1, 1), Direction.E, 60, 100);
        model.CreateState(At(2, 1), Direction.E, 60, 100); // l'arrivée, seule, est admissible

        StepOutcome outcome = model.EvaluateStep(start, Direction.E);

        Assert.Equal(StepRefusal.VolumeCollision, outcome.Refusal);
        Assert.Same(start, outcome.State);
    }

    /// <summary>
    /// Avenant n° 2, RL-02 (hors registre) : le volume est contrôlé sur chacun des deux segments du trajet en L,
    /// l'unité restant orientée vers le pas (A2, ARB-A, G1). Carte de 4 × 4 ; unité de 1 200 × 1 200 mm orientée N
    /// en (1,2) ; pas NE. Orientée NE, l'emprise est un carré posé sur la pointe, qui s'étend à 848,53 mm du centre
    /// selon x et selon y. Le passage N, prioritaire (A3), passe par (1,1) ; le passage E, par (2,2).
    /// - Mur sur l'arête nord de (0,2) : son extrémité est se trouve à 750 mm à l'ouest du 1er segment du passage N,
    ///   (1,2) → (1,1), à mi-chemin entre les deux centres.
    /// - Mur sur l'arête est de (1,0) : son extrémité sud se trouve à 750 mm au nord du 2e segment du passage N,
    ///   (1,1) → (2,1), à mi-chemin entre les deux centres.
    /// Dans chaque cas, le volume balayé par ce segment chevauche le mur de 98,53 mm, alors que l'unité orientée NE
    /// ne le touche ni au départ, ni dans la case intermédiaire (1,1), ni à l'arrivée (2,1). Aucun des deux murs n'est
    /// sur une arête traversée par le pas : le passage N est refusé au sens physique, et le pas emprunte le passage E.
    /// </summary>
    [Theory]
    [InlineData(0, 2, Direction.N)] // mur au bord du 1er segment du passage N
    [InlineData(1, 0, Direction.E)] // mur au bord du 2e segment du passage N
    public void RL02_VolumeIsCheckedOnBothLegsOfTheDiagonalPath(int wallColumn, int wallRow, Direction wallSide)
    {
        MovementModel open = Model(Map(4, 4), Square1200);
        Assert.Equal(Direction.N, open.EvaluateStep(open.CreateState(At(1, 2), Direction.N, 60, 100), Direction.NE).Passage);

        MovementModel model = Model(Map(4, 4).AddWall(At(wallColumn, wallRow), wallSide, WallType.Standard), Square1200);
        UnitState start = model.CreateState(At(1, 2), Direction.N, 60, 100);
        model.CreateState(At(1, 2), Direction.NE, 60, 100); // départ, orienté NE : admissible
        model.CreateState(At(1, 1), Direction.NE, 60, 100); // case intermédiaire du passage N : admissible
        model.CreateState(At(2, 1), Direction.NE, 60, 100); // arrivée : admissible

        StepOutcome outcome = model.EvaluateStep(start, Direction.NE);

        Assert.True(outcome.Accepted, outcome.Message);
        Assert.Equal(Direction.E, outcome.Passage);
        Assert.Equal(At(2, 1), outcome.State.Position);
    }
}
