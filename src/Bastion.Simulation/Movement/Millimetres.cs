namespace Bastion.Simulation.Movement;

/// <summary>
/// Validation des dimensions configurées : millimètres entiers (R-5), strictement positifs.
/// </summary>
internal static class Millimetres
{
    public static int RequirePositiveInteger(decimal value, string what, string parameterName)
    {
        if (value != decimal.Truncate(value))
        {
            throw new ArgumentException(
                $"{what} doit être un nombre entier de millimètres (R-5) ; valeur reçue : {value} mm.",
                parameterName);
        }

        if (value <= 0 || value > int.MaxValue)
        {
            throw new ArgumentOutOfRangeException(
                parameterName,
                value,
                $"{what} doit être un nombre de millimètres strictement positif ; valeur reçue : {value} mm.");
        }

        return (int)value;
    }
}
