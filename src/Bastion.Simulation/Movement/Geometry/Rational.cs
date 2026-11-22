using System.Numerics;

namespace Bastion.Simulation.Movement.Geometry;

/// <summary>
/// Nombre rationnel exact, toujours réduit, de dénominateur strictement positif.
/// Les calculs physiques ne sont pas limités systématiquement aux entiers (R-5) ; le calcul exact
/// permet de distinguer le contact du chevauchement sans introduire de tolérance numérique.
/// </summary>
internal readonly struct Rational : IComparable<Rational>
{
    private readonly BigInteger _denominator;

    private Rational(BigInteger numerator, BigInteger denominator)
    {
        Numerator = numerator;
        _denominator = denominator;
    }

    public BigInteger Numerator { get; }

    /// <summary>Dénominateur ; la valeur par défaut de la structure vaut 0/1.</summary>
    public BigInteger Denominator => _denominator.IsZero ? BigInteger.One : _denominator;

    public static Rational Zero => default;

    public static Rational Half => new(BigInteger.One, 2);

    public int Sign => Numerator.Sign;

    public static Rational Of(BigInteger numerator, BigInteger denominator)
    {
        if (denominator.IsZero)
        {
            throw new DivideByZeroException("Division par zéro dans un calcul géométrique.");
        }

        if (denominator.Sign < 0)
        {
            numerator = -numerator;
            denominator = -denominator;
        }

        BigInteger divisor = BigInteger.GreatestCommonDivisor(numerator, denominator);
        if (divisor > BigInteger.One)
        {
            numerator /= divisor;
            denominator /= divisor;
        }

        return new Rational(numerator, denominator);
    }

    public static implicit operator Rational(long value) => new(value, BigInteger.One);

    public static Rational operator +(Rational a, Rational b) =>
        Of(a.Numerator * b.Denominator + b.Numerator * a.Denominator, a.Denominator * b.Denominator);

    public static Rational operator -(Rational a, Rational b) =>
        Of(a.Numerator * b.Denominator - b.Numerator * a.Denominator, a.Denominator * b.Denominator);

    public static Rational operator -(Rational a) => new(-a.Numerator, a.Denominator);

    public static Rational operator *(Rational a, Rational b) =>
        Of(a.Numerator * b.Numerator, a.Denominator * b.Denominator);

    public static Rational operator /(Rational a, Rational b) =>
        Of(a.Numerator * b.Denominator, a.Denominator * b.Numerator);

    public int CompareTo(Rational other) =>
        (Numerator * other.Denominator).CompareTo(other.Numerator * Denominator);

    public override string ToString() => Denominator.IsOne ? Numerator.ToString() : $"{Numerator}/{Denominator}";
}
