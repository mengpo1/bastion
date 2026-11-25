using Bastion.Simulation.Movement;

namespace Bastion.Simulation.Turns;

/// <summary>
/// État de la gestion des tours (MEC-0004) : numéro du tour courant et état de l'unité (position, orientation, TU,
/// énergie). Immuable ; se crée par <see cref="TurnRules.Start"/>, qui le valide.
/// </summary>
public sealed record TurnState
{
    internal TurnState(int turn, UnitState unit)
    {
        Turn = turn;
        Unit = unit;
    }

    /// <summary>Numéro du tour courant ; le premier tour porte le numéro 1.</summary>
    public int Turn { get; }

    public UnitState Unit { get; }
}

/// <summary>Résultat d'une fin de tour : états avant et après, récupérations effectives et compte rendu (§3.4).</summary>
public sealed record TurnOutcome
{
    internal TurnOutcome(TurnState before, TurnState after)
    {
        Before = before;
        After = after;
    }

    public TurnState Before { get; }

    public TurnState After { get; }

    /// <summary>TU effectivement récupérées, après plafonnement.</summary>
    public int RecoveredTu => After.Unit.Tu - Before.Unit.Tu;

    /// <summary>Énergie effectivement récupérée, après plafonnement.</summary>
    public int RecoveredEnergy => After.Unit.Energy - Before.Unit.Energy;

    /// <summary>Compte rendu de la fin de tour et de la récupération effectuée (§3.4).</summary>
    public string Message =>
        $"Fin du tour {Before.Turn} : {RecoveredTu} TU et {RecoveredEnergy} d'énergie récupérées. Début du tour {After.Turn}.";
}
