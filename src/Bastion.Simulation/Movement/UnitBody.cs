namespace Bastion.Simulation.Movement;

/// <summary>
/// Emprise rectangulaire de l'unité, configurable par type (Q1.2), orientée selon A8 :
/// largeur perpendiculaire à la direction de face, profondeur parallèle, hauteur verticale.
/// Dans MEC-0003, le contrôle se fait en plan (A2) : la hauteur est conservée mais n'intervient pas.
/// </summary>
public sealed record UnitBody
{
    public UnitBody(decimal widthMm, decimal depthMm, decimal heightMm)
    {
        WidthMm = Millimetres.RequirePositiveInteger(widthMm, "La largeur de l'unité", nameof(widthMm));
        DepthMm = Millimetres.RequirePositiveInteger(depthMm, "La profondeur de l'unité", nameof(depthMm));
        HeightMm = Millimetres.RequirePositiveInteger(heightMm, "La hauteur de l'unité", nameof(heightMm));
    }

    /// <summary>Profil humain initial, debout : 600 × 600 × 1 800 mm (Q1.6).</summary>
    public static UnitBody StandardHuman { get; } = new(600m, 600m, 1800m);

    public int WidthMm { get; }

    public int DepthMm { get; }

    public int HeightMm { get; }
}
