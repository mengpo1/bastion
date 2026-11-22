namespace Bastion.Simulation.Movement;

/// <summary>
/// Type de mur : mur plein, infranchissable, de pleine hauteur, d'épaisseur configurable par type
/// (Q1.3 ; 100 mm initialement, Q1.7). Les murs possèdent un volume physique : l'épaisseur est non nulle.
/// </summary>
public sealed record WallType
{
    public WallType(string name, decimal thicknessMm)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(name);
        Name = name;
        ThicknessMm = Millimetres.RequirePositiveInteger(thicknessMm, $"L'épaisseur du mur « {name} »", nameof(thicknessMm));
    }

    /// <summary>Mur standard de 100 mm (Q1.7).</summary>
    public static WallType Standard { get; } = new("standard", 100m);

    public string Name { get; }

    public int ThicknessMm { get; }
}
