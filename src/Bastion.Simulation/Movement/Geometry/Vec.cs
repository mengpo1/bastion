namespace Bastion.Simulation.Movement.Geometry;

/// <summary>
/// Vecteur ou point du plan, en millimètres. Repère : x vers l'est, y vers le sud.
/// </summary>
internal readonly record struct Vec(Surd X, Surd Y)
{
    public static Vec operator +(Vec a, Vec b) => new(a.X + b.X, a.Y + b.Y);

    public static Vec operator -(Vec a, Vec b) => new(a.X - b.X, a.Y - b.Y);

    public static Vec operator *(Vec a, Surd factor) => new(a.X * factor, a.Y * factor);

    public Surd Dot(Vec other) => X * other.X + Y * other.Y;

    public Surd Cross(Vec other) => X * other.Y - Y * other.X;
}
