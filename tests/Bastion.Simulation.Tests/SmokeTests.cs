using System.Reflection;

namespace Bastion.Simulation.Tests;

/// <summary>
/// Tests fumée techniques. Aucune logique de jeu.
/// </summary>
public class SmokeTests
{
    private static readonly Assembly Simulation = typeof(SimulationAssembly).Assembly;

    [Fact]
    public void SimulationAssemblyIsLoaded()
    {
        Assert.Equal("Bastion.Simulation", Simulation.GetName().Name);
    }

    // Détecte l'usage d'un type Godot dans la simulation. Une référence de paquet Godot
    // déclarée mais inutilisée n'apparaît pas dans l'assembly et n'est pas détectée.
    [Fact]
    public void SimulationDoesNotReferenceGodot()
    {
        var godotReferences = Simulation.GetReferencedAssemblies()
            .Where(reference => reference.Name?.StartsWith("Godot", StringComparison.OrdinalIgnoreCase) == true);

        Assert.Empty(godotReferences);
    }
}
