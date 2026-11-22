namespace Bastion.Simulation.Movement;

/// <summary>Coût d'un pas, en TU et en énergie.</summary>
public readonly record struct StepCost(int Tu, int Energy);

/// <summary>
/// Barème de la marche : base en TU et en énergie (Q3.7 ; 4 TU et 2 d'énergie initialement) et
/// multiplicateur d'énergie des diagonales, propre et configurable (Q3.2 ; 1,5 initialement, Q3.9).
/// Le multiplicateur des TU des diagonales est celui de S2 : 1,5, arrondi inférieur.
/// </summary>
public sealed record MovementRules
{
    public MovementRules(int baseTu, int baseEnergy, decimal diagonalEnergyMultiplier)
    {
        if (baseTu < 1)
        {
            throw new ArgumentOutOfRangeException(
                nameof(baseTu),
                baseTu,
                "Le coût de base en TU doit valoir au moins 1 : un pas à 0 TU est refusé dans MEC-0003 (A4 d).");
        }

        if (baseEnergy < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(baseEnergy), baseEnergy, "Le coût de base en énergie ne peut pas être négatif.");
        }

        if (diagonalEnergyMultiplier < 0)
        {
            throw new ArgumentOutOfRangeException(
                nameof(diagonalEnergyMultiplier),
                diagonalEnergyMultiplier,
                "Le multiplicateur d'énergie des diagonales ne peut pas être négatif.");
        }

        BaseTu = baseTu;
        BaseEnergy = baseEnergy;
        DiagonalEnergyMultiplier = diagonalEnergyMultiplier;
    }

    /// <summary>Valeurs initiales : 4 TU, 2 d'énergie, multiplicateur d'énergie des diagonales de 1,5.</summary>
    public static MovementRules Initial { get; } = new(4, 2, 1.5m);

    public int BaseTu { get; }

    public int BaseEnergy { get; }

    public decimal DiagonalEnergyMultiplier { get; }

    /// <summary>
    /// Coût d'un pas selon le terrain de la case d'arrivée (S2, Q3.1). Ordre des arrondis (Q3.13) :
    /// la base de chaque ressource est multipliée par le facteur du terrain, puis arrondie à l'entier
    /// supérieur ; ensuite, pour une diagonale, TU × 1,5 arrondi à l'entier inférieur (S2) et énergie ×
    /// multiplicateur propre arrondi à l'entier supérieur (Q3.2, Q3.9).
    /// </summary>
    public StepCost CostOf(Direction direction, TerrainType arrival)
    {
        ArgumentNullException.ThrowIfNull(arrival);
        int tu = (int)decimal.Ceiling(BaseTu * arrival.Factor);
        int energy = (int)decimal.Ceiling(BaseEnergy * arrival.Factor);
        if (!direction.IsDiagonal())
        {
            return new StepCost(tu, energy);
        }

        return new StepCost((int)decimal.Floor(tu * 1.5m), (int)decimal.Ceiling(energy * DiagonalEnergyMultiplier));
    }
}
