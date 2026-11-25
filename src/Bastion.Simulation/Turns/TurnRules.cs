using Bastion.Simulation.Movement;

namespace Bastion.Simulation.Turns;

/// <summary>
/// Gestion élémentaire des tours d'une seule unité (MEC-0004) : plafonds et récupérations par tour des TU et de
/// l'énergie, configurables (§3.1), et fin de tour explicite (§3.3). Immuable. Les valeurs initiales forment un
/// profil de test (Q4.6), et non l'équilibrage définitif. Le moteur de marche (MEC-0003) n'est pas modifié : les états
/// qu'il rend sont repris tels quels par <see cref="WithUnit"/>.
/// </summary>
public sealed record TurnRules
{
    /// <summary>
    /// Crée des paramètres validés (§3.2) : plafonds strictement positifs, récupérations positives ou nulles. Une
    /// récupération supérieure au plafond est autorisée.
    /// </summary>
    public TurnRules(int maxTu, int tuRecovery, int maxEnergy, int energyRecovery)
    {
        RequireStrictlyPositive(maxTu, "Le plafond de TU", nameof(maxTu));
        RequirePositiveOrZero(tuRecovery, "La récupération de TU", nameof(tuRecovery));
        RequireStrictlyPositive(maxEnergy, "Le plafond d'énergie", nameof(maxEnergy));
        RequirePositiveOrZero(energyRecovery, "La récupération d'énergie", nameof(energyRecovery));
        MaxTu = maxTu;
        TuRecovery = tuRecovery;
        MaxEnergy = maxEnergy;
        EnergyRecovery = energyRecovery;
    }

    /// <summary>Profil initial de test (Q4.6) : 60 TU maximales, 60 récupérées par tour, 100 d'énergie maximale, 20 récupérées.</summary>
    public static TurnRules Initial { get; } = new(60, 60, 100, 20);

    public int MaxTu { get; }

    public int TuRecovery { get; }

    public int MaxEnergy { get; }

    public int EnergyRecovery { get; }

    /// <summary>
    /// Commence la gestion des tours au tour 1 (§3.3) avec l'état donné. Un état dont une ressource est négative ou
    /// dépasse son plafond est refusé, sans réduction silencieuse ; un état exactement aux plafonds est accepté (§3.2).
    /// </summary>
    public TurnState Start(UnitState unit) => new(1, RequireWithinCaps(unit));

    /// <summary>
    /// Remplace l'état de l'unité dans le tour courant, par exemple par l'état rendu par le moteur de marche après un
    /// déplacement. Le numéro de tour ne change pas ; le nouvel état est validé comme au départ (§3.2).
    /// </summary>
    public TurnState WithUnit(TurnState state, UnitState unit)
    {
        ArgumentNullException.ThrowIfNull(state);
        return new TurnState(state.Turn, RequireWithinCaps(unit));
    }

    /// <summary>
    /// Fin de tour explicite (§3.3), autorisée sans action préalable et même aux plafonds : chaque ressource vaut
    /// min(courante + récupération, plafond), indépendamment de l'autre (§3.1) ; le numéro de tour augmente de 1 ; la
    /// position et l'orientation sont conservées. Rend un nouvel état ; l'état donné n'est pas modifié.
    /// </summary>
    public TurnOutcome EndTurn(TurnState state)
    {
        ArgumentNullException.ThrowIfNull(state);
        UnitState unit = RequireWithinCaps(state.Unit);
        UnitState recovered = unit with
        {
            Tu = CappedSum(unit.Tu, TuRecovery, MaxTu),
            Energy = CappedSum(unit.Energy, EnergyRecovery, MaxEnergy),
        };
        return new TurnOutcome(state, new TurnState(checked(state.Turn + 1), recovered));
    }

    /// <summary>Addition plafonnée, calculée sur 64 bits : aucun débordement, même avec une récupération très grande.</summary>
    private static int CappedSum(int current, int recovery, int max) => (int)Math.Min((long)current + recovery, max);

    private UnitState RequireWithinCaps(UnitState unit)
    {
        ArgumentNullException.ThrowIfNull(unit);
        if (unit.Tu < 0 || unit.Tu > MaxTu || unit.Energy < 0 || unit.Energy > MaxEnergy)
        {
            throw new ArgumentException(
                $"Ressources hors des plafonds : {unit.Tu} TU pour un plafond de {MaxTu}, {unit.Energy} d'énergie pour un plafond de {MaxEnergy}. "
                + "Chaque ressource doit être comprise entre 0 et son plafond (MEC-0004, §3.2).",
                nameof(unit));
        }

        return unit;
    }

    private static void RequireStrictlyPositive(int value, string what, string parameterName)
    {
        if (value <= 0)
        {
            throw new ArgumentOutOfRangeException(parameterName, value, $"{what} doit être strictement positif (MEC-0004, §3.2).");
        }
    }

    private static void RequirePositiveOrZero(int value, string what, string parameterName)
    {
        if (value < 0)
        {
            throw new ArgumentOutOfRangeException(parameterName, value, $"{what} ne peut pas être négative (MEC-0004, §3.2).");
        }
    }
}
