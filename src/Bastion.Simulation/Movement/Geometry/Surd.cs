namespace Bastion.Simulation.Movement.Geometry;

/// <summary>
/// Nombre exact de la forme a + b√2, a et b rationnels. Il suffit à décrire les emprises orientées
/// selon les huit directions (multiples de 45°), et son signe se calcule exactement.
/// </summary>
internal readonly struct Surd : IComparable<Surd>
{
    public Surd(Rational rational, Rational root)
    {
        A = rational;
        B = root;
    }

    /// <summary>Partie rationnelle a.</summary>
    public Rational A { get; }

    /// <summary>Coefficient b de √2.</summary>
    public Rational B { get; }

    public static Surd Zero => default;

    /// <summary>√2 / 2, valeur de cos 45° et de sin 45°.</summary>
    public static Surd HalfRoot2 => new(Rational.Zero, Rational.Half);

    /// <summary>Signe exact : 1, 0 ou -1.</summary>
    public int Sign
    {
        get
        {
            int signA = A.Sign;
            int signB = B.Sign;
            if (signB == 0)
            {
                return signA;
            }

            if (signA == 0 || signA == signB)
            {
                return signB;
            }

            // Signes opposés : comparer |a| et |b|·√2 par leurs carrés (√2 est irrationnel, l'égalité est impossible).
            int comparison = (A * A).CompareTo(2 * (B * B));
            return signA > 0 ? comparison : -comparison;
        }
    }

    public static implicit operator Surd(Rational value) => new(value, Rational.Zero);

    public static implicit operator Surd(long value) => new(value, Rational.Zero);

    public static Surd operator +(Surd x, Surd y) => new(x.A + y.A, x.B + y.B);

    public static Surd operator -(Surd x, Surd y) => new(x.A - y.A, x.B - y.B);

    public static Surd operator -(Surd x) => new(-x.A, -x.B);

    public static Surd operator *(Surd x, Surd y) =>
        new(x.A * y.A + 2 * (x.B * y.B), x.A * y.B + x.B * y.A);

    public static Surd operator /(Surd x, Surd y)
    {
        // (a + b√2) / (c + e√2) = (a + b√2)(c − e√2) / (c² − 2e²).
        Rational norm = y.A * y.A - 2 * (y.B * y.B);
        if (norm.Sign == 0)
        {
            throw new DivideByZeroException("Division par zéro dans un calcul géométrique.");
        }

        return new Surd((x.A * y.A - 2 * (x.B * y.B)) / norm, (x.B * y.A - x.A * y.B) / norm);
    }

    public int CompareTo(Surd other) => (this - other).Sign;

    public static Surd Min(Surd x, Surd y) => x.CompareTo(y) <= 0 ? x : y;

    public static Surd Max(Surd x, Surd y) => x.CompareTo(y) >= 0 ? x : y;

    public override string ToString() => B.Sign == 0 ? A.ToString() : $"{A} + {B}√2";
}
