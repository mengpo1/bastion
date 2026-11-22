namespace Bastion.Simulation.Movement.Geometry;

/// <summary>
/// Pavé d'obstacle aligné sur les axes, vu en plan : mur, case infranchissable ou bord de la carte.
/// Les obstacles de MEC-0003 sont de pleine hauteur ; le contrôle se fait en plan (A2).
/// </summary>
internal readonly record struct Box(Rational MinX, Rational MinY, Rational MaxX, Rational MaxY)
{
    public Vec[] Corners() =>
    [
        new Vec(MinX, MinY),
        new Vec(MaxX, MinY),
        new Vec(MaxX, MaxY),
        new Vec(MinX, MaxY),
    ];
}
