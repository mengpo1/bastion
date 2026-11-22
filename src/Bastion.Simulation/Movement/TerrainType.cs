namespace Bastion.Simulation.Movement;

/// <summary>
/// Type de terrain : un facteur unique, commun aux TU et à l'énergie (A6, Q3.1). Le facteur
/// multiplie la base de chaque ressource ; chaque résultat est arrondi séparément (Q3.13).
/// </summary>
public sealed record TerrainType
{
    public TerrainType(string name, decimal factor)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(name);
        if (factor <= 0)
        {
            throw new ArgumentOutOfRangeException(
                nameof(factor),
                factor,
                $"Le facteur du terrain « {name} » doit être strictement positif : un facteur nul ou négatif "
                + "permettrait un pas à 0 TU, refusé dans MEC-0003 (A4 d).");
        }

        Name = name;
        Factor = factor;
    }

    /// <summary>Terrain normal : coût de base (Q3.8).</summary>
    public static TerrainType Normal { get; } = new("normal", 1m);

    /// <summary>Terrain difficile : +50 % de TU et d'énergie (Q3.8).</summary>
    public static TerrainType Difficult { get; } = new("difficile", 1.5m);

    /// <summary>Terrain très difficile : +100 % (Q3.8).</summary>
    public static TerrainType VeryDifficult { get; } = new("très difficile", 2m);

    public string Name { get; }

    public decimal Factor { get; }
}
