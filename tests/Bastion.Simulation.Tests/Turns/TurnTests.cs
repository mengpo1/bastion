using Bastion.Simulation.Movement;
using Bastion.Simulation.Turns;
using static Bastion.Simulation.Tests.Movement.TestWorld;

namespace Bastion.Simulation.Tests.Turns;

/// <summary>
/// Tests de MEC-0004 pour la partie moteur : T01 à T09, T14 et T15 (T05 pour la part du moteur). Les valeurs attendues
/// sont celles de la fiche, écrites en constantes. T10 à T13 et T16, qui portent sur le prototype Godot, sont vérifiés
/// par son contrôle fumée.
/// </summary>
public class TurnTests
{
    /// <summary>Carte du scénario 1 du prototype : 5 × 5 cases, (3,2) infranchissable.</summary>
    private static readonly MovementModel Walk = Model(Map(5, 5).Block(At(3, 2)));

    private static UnitState Unit(int tu, int energy) => Walk.CreateState(At(1, 4), Direction.N, tu, energy);

    private static void AssertResources(TurnState state, int turn, int tu, int energy)
    {
        Assert.Equal(turn, state.Turn);
        Assert.Equal(tu, state.Unit.Tu);
        Assert.Equal(energy, state.Unit.Energy);
    }

    [Fact]
    public void InitialProfileIsTheTestProfileOfTheCard()
    {
        Assert.Equal(new TurnRules(60, 60, 100, 20), TurnRules.Initial);
    }

    [Fact]
    public void T01_EndOfTurnFrom12TuAnd35Energy()
    {
        TurnState start = TurnRules.Initial.Start(Unit(12, 35));
        AssertResources(start, 1, 12, 35);

        TurnOutcome outcome = TurnRules.Initial.EndTurn(start);

        AssertResources(outcome.After, 2, 60, 55);
        Assert.Equal(48, outcome.RecoveredTu);
        Assert.Equal(20, outcome.RecoveredEnergy);
        Assert.Same(start, outcome.Before);
    }

    [Fact]
    public void T02_NextEndOfTurnWithoutMovement()
    {
        TurnState turn2 = TurnRules.Initial.EndTurn(TurnRules.Initial.Start(Unit(12, 35))).After;
        AssertResources(turn2, 2, 60, 55);

        AssertResources(TurnRules.Initial.EndTurn(turn2).After, 3, 60, 75);
    }

    [Fact]
    public void T03_BothResourcesAreCapped()
    {
        TurnOutcome outcome = TurnRules.Initial.EndTurn(TurnRules.Initial.Start(Unit(58, 95)));

        AssertResources(outcome.After, 2, 60, 100);
        Assert.Equal(2, outcome.RecoveredTu);
        Assert.Equal(5, outcome.RecoveredEnergy);
    }

    [Fact]
    public void T04_TurnCounterIncreasesByOneWithoutMovement()
    {
        TurnState state = TurnRules.Initial.Start(Unit(12, 35));
        for (int expected = 2; expected <= 5; expected++)
        {
            state = TurnRules.Initial.EndTurn(state).After;
            Assert.Equal(expected, state.Turn);
        }
    }

    [Fact]
    public void T05_PositionAndOrientationAreKeptAfterAMovement()
    {
        TurnState start = TurnRules.Initial.Start(Unit(12, 35));
        OrderOutcome order = Walk.ExecuteOrder(start.Unit, At(2, 4));
        Assert.Equal(At(2, 4), order.FinalState.Position);
        Assert.Equal(Direction.E, order.FinalState.Orientation);
        TurnState moved = TurnRules.Initial.WithUnit(start, order.FinalState);
        Assert.Equal(1, moved.Turn);

        TurnState after = TurnRules.Initial.EndTurn(moved).After;

        Assert.Equal(At(2, 4), after.Unit.Position);
        Assert.Equal(Direction.E, after.Unit.Orientation);
        AssertResources(after, 2, 60, Math.Min(order.FinalState.Energy + 20, 100));
    }

    [Fact]
    public void WithUnitKeepsTheTurnNumberAfterTheFirstTurn()
    {
        TurnState turn2 = TurnRules.Initial.EndTurn(TurnRules.Initial.Start(Unit(12, 35))).After;
        OrderOutcome order = Walk.ExecuteOrder(turn2.Unit, At(2, 4));

        TurnState moved = TurnRules.Initial.WithUnit(turn2, order.FinalState);

        Assert.Equal(2, moved.Turn);
        Assert.Equal(order.FinalState, moved.Unit);
        Assert.Equal(3, TurnRules.Initial.EndTurn(moved).After.Turn);
    }

    [Fact]
    public void T06_CustomParametersAreApplied()
    {
        var rules = new TurnRules(maxTu: 40, tuRecovery: 25, maxEnergy: 30, energyRecovery: 10);

        AssertResources(rules.EndTurn(rules.Start(Unit(12, 15))).After, 2, 37, 25);
    }

    [Fact]
    public void T07_RecoveryAboveTheCapIsAllowedAndCapped()
    {
        var rules = new TurnRules(maxTu: 60, tuRecovery: 100, maxEnergy: 100, energyRecovery: 150);
        AssertResources(rules.EndTurn(rules.Start(Unit(10, 5))).After, 2, 60, 100);

        // Récupérations maximales : l'addition plafonnée ne déborde pas.
        var huge = new TurnRules(60, int.MaxValue, 100, int.MaxValue);
        AssertResources(huge.EndTurn(huge.Start(Unit(60, 100))).After, 2, 60, 100);
        AssertResources(huge.EndTurn(huge.Start(Unit(0, 0))).After, 2, 60, 100);
    }

    [Fact]
    public void T08_ZeroRecoveryLeavesTheResourceUnchanged()
    {
        var noTu = new TurnRules(60, 0, 100, 20);
        AssertResources(noTu.EndTurn(noTu.Start(Unit(12, 35))).After, 2, 12, 55);

        var noEnergy = new TurnRules(60, 60, 100, 0);
        AssertResources(noEnergy.EndTurn(noEnergy.Start(Unit(12, 35))).After, 2, 60, 35);
    }

    [Fact]
    public void T09_NegativeParametersAreRefused()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new TurnRules(-1, 60, 100, 20));
        Assert.Throws<ArgumentOutOfRangeException>(() => new TurnRules(60, -1, 100, 20));
        Assert.Throws<ArgumentOutOfRangeException>(() => new TurnRules(60, 60, -1, 20));
        Assert.Throws<ArgumentOutOfRangeException>(() => new TurnRules(60, 60, 100, -1));
    }

    [Fact]
    public void T09_ZeroCapsAreRefused()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new TurnRules(0, 60, 100, 20));
        Assert.Throws<ArgumentOutOfRangeException>(() => new TurnRules(60, 60, 0, 20));
    }

    [Fact]
    public void T09_InitialStateAboveACapIsRefusedWithoutSilentReduction()
    {
        var tuError = Assert.Throws<ArgumentException>(() => TurnRules.Initial.Start(Unit(61, 35)));
        Assert.Contains("plafond", tuError.Message);
        Assert.Throws<ArgumentException>(() => TurnRules.Initial.Start(Unit(12, 101)));
    }

    [Fact]
    public void T09_NegativeResourcesAreRefused()
    {
        Assert.Throws<ArgumentException>(() => TurnRules.Initial.Start(Unit(12, 35) with { Tu = -1 }));
        Assert.Throws<ArgumentException>(() => TurnRules.Initial.Start(Unit(12, 35) with { Energy = -1 }));
    }

    [Fact]
    public void T09_RejectionLeavesTheStateUnchanged()
    {
        TurnState state = TurnRules.Initial.Start(Unit(12, 35));
        UnitState before = state.Unit;

        Assert.Throws<ArgumentException>(() => TurnRules.Initial.WithUnit(state, Unit(61, 35)));

        // Un état valide pour un profil, mais hors des plafonds d'un autre, est refusé par ce dernier.
        var smaller = new TurnRules(10, 10, 10, 10);
        Assert.Throws<ArgumentException>(() => smaller.EndTurn(state));

        Assert.Equal(1, state.Turn);
        Assert.Same(before, state.Unit);
        AssertResources(state, 1, 12, 35);
    }

    [Fact]
    public void T14_EndOfTurnAtTheCapsKeepsResourcesAndIncrementsTheCounter()
    {
        TurnOutcome outcome = TurnRules.Initial.EndTurn(TurnRules.Initial.Start(Unit(60, 100)));

        AssertResources(outcome.After, 2, 60, 100);
        Assert.Equal(0, outcome.RecoveredTu);
        Assert.Equal(0, outcome.RecoveredEnergy);
    }

    [Fact]
    public void T15_InitialStateExactlyAtTheCapsIsAccepted()
    {
        AssertResources(TurnRules.Initial.Start(Unit(60, 100)), 1, 60, 100);

        var rules = new TurnRules(40, 25, 30, 10);
        AssertResources(rules.Start(Unit(40, 30)), 1, 40, 30);
        AssertResources(rules.Start(Unit(0, 0)), 1, 0, 0);
    }

    [Fact]
    public void EndOfTurnReturnsANewStateAndLeavesTheGivenOneUnchanged()
    {
        TurnState start = TurnRules.Initial.Start(Unit(12, 35));

        TurnState after = TurnRules.Initial.EndTurn(start).After;

        Assert.NotSame(start, after);
        AssertResources(start, 1, 12, 35);
        Assert.Equal(start.Unit.Position, after.Unit.Position);
        Assert.Equal(start.Unit.Orientation, after.Unit.Orientation);
    }

    [Fact]
    public void EndOfTurnMessageReportsTheRecovery()
    {
        TurnOutcome outcome = TurnRules.Initial.EndTurn(TurnRules.Initial.Start(Unit(12, 35)));

        Assert.Equal("Fin du tour 1 : 48 TU et 20 d'énergie récupérées. Début du tour 2.", outcome.Message);
    }
}
