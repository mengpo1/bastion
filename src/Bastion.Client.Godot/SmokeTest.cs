using Bastion.Simulation.Movement;
using Godot;

namespace Bastion.Client;

/// <summary>
/// Contrôle fumée du prototype (lot 1D), lancé par l'argument utilisateur « --smoke-test ».
/// Il envoie des clics et des touches à la fenêtre (<see cref="Viewport.PushInput"/>), traités par le même code que
/// ceux du joueur (<see cref="PrototypeScene._UnhandledInput"/>), puis compare l'état de la scène et le texte de son
/// panneau aux résultats du moteur et aux valeurs du mandat. Le dessin (grille, zone, unité) n'est pas contrôlé ici :
/// seules les captures le montrent. Ce contrôle ne prouve pas à lui seul que la scène ne contient aucune règle de
/// jeu : c'est la lecture de son code qui l'établit.
/// Code de sortie : 0 si tous les contrôles réussissent, 1 sinon, 2 en cas d'exception. Si la scène ne peut pas
/// démarrer (projet non compilé en Debug, par exemple), ce contrôle ne s'exécute pas : lancer Godot avec une limite
/// de temps (voir README.md).
/// Avec « --capture=&lt;dossier&gt; », une image de la fenêtre est enregistrée après chaque étape ; cela demande
/// un rendu réel, donc un affichage : en mode headless, la demande de capture est un échec.
/// </summary>
internal static class SmokeTest
{
    private static readonly GridPosition FirstDestination = new(2, 4);
    private static readonly GridPosition Blocked = new(3, 2);
    private static readonly GridPosition OutOfZone = new(4, 0);
    private static readonly GridPosition SecondDestination = new(2, 2);
    private static readonly Vector2 RightOfTheMap = new(700f, 300f);
    private static readonly Vector2 LeftOfTheMap = new(12f, 300f);

    public static async Task RunAsync(PrototypeScene scene)
    {
        int failures = 0;
        void Check(bool condition, string description)
        {
            GD.Print($"SMOKE {(condition ? "OK" : "ÉCHEC")} : {description}");
            if (!condition)
            {
                failures++;
            }
        }

        try
        {
            string? captureDirectory = OS.GetCmdlineUserArgs()
                .FirstOrDefault(argument => argument.StartsWith("--capture=", StringComparison.Ordinal))?["--capture=".Length..];
            if (captureDirectory is not null && DisplayServer.GetName() == "headless")
            {
                Check(false, "capture demandée en mode headless : impossible sans affichage");
                captureDirectory = null;
            }

            int step = 0;
            async Task Settle(string name)
            {
                await scene.ToSignal(scene.GetTree(), SceneTree.SignalName.ProcessFrame);
                await scene.ToSignal(scene.GetTree(), SceneTree.SignalName.ProcessFrame);
                if (captureDirectory is not null)
                {
                    await scene.ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
                    step++;
                    string path = $"{captureDirectory}/{step:00}-{name}.png";
                    Error saved = scene.GetViewport().GetTexture().GetImage().SavePng(path);
                    Check(saved == Error.Ok, $"capture {path}");
                }
            }

            void CheckHud(string when)
            {
                UnitState state = scene.State;
                string hud = scene.HudText;
                Check(hud.Contains($"Position : {state.Position}\n", StringComparison.Ordinal)
                    && hud.Contains($"Orientation : {state.Orientation}\n", StringComparison.Ordinal)
                    && hud.Contains($"TU restantes : {state.Tu}\n", StringComparison.Ordinal)
                    && hud.Contains($"Énergie restante : {state.Energy}\n", StringComparison.Ordinal)
                    && hud.Contains($"Dernier résultat : {scene.LastResult}\n", StringComparison.Ordinal),
                    $"panneau conforme à l'état {when}");
            }

            Godot.Collections.Dictionary version = Engine.GetVersionInfo();
            Check(version["major"].AsInt32() == 4 && version["minor"].AsInt32() == 7 && version["patch"].AsInt32() == 2
                && version["status"].AsString() == "stable", $"version de Godot épinglée 4.7.2 stable ({version["string"].AsString()})");

            // Scénario du mandat 1D, §4.1 : carte de 5 × 5 cases de 1 500 mm, seule (3,2) infranchissable.
            MovementModel model = scene.Model;
            TacticalMap map = model.Map;
            var blockedCells = new List<GridPosition>();
            for (int row = 0; row < map.Rows; row++)
            {
                for (int column = 0; column < map.Columns; column++)
                {
                    if (map.IsBlocked(new GridPosition(column, row)))
                    {
                        blockedCells.Add(new GridPosition(column, row));
                    }
                }
            }

            Check(map.Columns == 5 && map.Rows == 5 && map.CellWidthMm == 1500 && blockedCells.SequenceEqual([Blocked])
                && model.Body == UnitBody.StandardHuman,
                $"carte de {map.Columns} × {map.Rows} cases de {map.CellWidthMm} mm, case infranchissable {string.Join(" ", blockedCells)}, unité de {model.Body.WidthMm} × {model.Body.DepthMm} × {model.Body.HeightMm} mm (StandardHuman attendue)");

            await Settle("initial");
            UnitState initial = scene.State;
            // Valeurs attendues fixées par le mandat 1D, indépendamment des constantes de la scène.
            Check(Same(initial, new GridPosition(1, 4), Direction.N, 20, 10),
                $"état initial (1,4), N, 20 TU, 10 d'énergie : {Describe(initial)}");
            HashSet<GridPosition> initialZone = scene.Reachability.Zone.ToHashSet();
            Check(initialZone.Count > 0 && initialZone.SetEquals(model.ComputeReachability(initial).Zone),
                $"zone affichée = zone du moteur ({initialZone.Count} cases)");
            CheckHud("initial");

            // 1er ordre : clic sur (2,4), comparé au résultat réel d'ExecuteOrder depuis l'état initial.
            OrderOutcome expectedFirst = model.ExecuteOrder(initial, FirstDestination);
            Click(scene, PrototypeScene.CellCenter(FirstDestination));
            await Settle("ordre-2-4");
            Check(scene.State == expectedFirst.FinalState && scene.LastResult == expectedFirst.Message,
                $"clic sur (2,4) = résultat d'ExecuteOrder : {Describe(scene.State)} ({scene.LastResult})");
            Check(Same(scene.State, FirstDestination, Direction.E, 16, 8), "arrivée en (2,4), E, 16 TU, 8 d'énergie");
            CheckHud("après le 1er ordre");

            // Clics sans effet : chacun doit atteindre la scène (message attendu) sans changer l'état.
            UnitState beforeRefusals = scene.State;
            Check(!scene.Reachability.Contains(Blocked) && !scene.Reachability.Contains(OutOfZone),
                "(3,2) et (4,0) sont hors de la zone du moteur");
            // Deux clics consécutifs donnent toujours deux messages différents : chacun prouve que le clic est arrivé.
            const string OutsideMessage = "Clic hors de la carte : aucun ordre transmis.";
            foreach ((Vector2 position, string expectedMessage, string name, string slug) in new[]
            {
                (PrototypeScene.CellCenter(FirstDestination), model.ExecuteOrder(beforeRefusals, FirstDestination).Message,
                    "sur la case de l'unité", "case-unite"),
                (RightOfTheMap, OutsideMessage, "à droite de la carte", "hors-carte-droite"),
                (PrototypeScene.CellCenter(Blocked), model.ExecuteOrder(beforeRefusals, Blocked).Message,
                    "sur la case infranchissable (3,2)", "case-bloquee"),
                (LeftOfTheMap, OutsideMessage, "à gauche de la carte", "hors-carte-gauche"),
                (PrototypeScene.CellCenter(OutOfZone), model.ExecuteOrder(beforeRefusals, OutOfZone).Message,
                    "sur la case hors zone (4,0)", "hors-zone"),
            })
            {
                Click(scene, position);
                await Settle($"clic-{slug}");
                Check(scene.State == beforeRefusals && scene.LastResult == expectedMessage,
                    $"clic {name} : état inchangé ({scene.LastResult})");
            }

            CheckHud("après les clics refusés");

            // 2e ordre : les ressources restantes sont utilisées et la zone est recalculée.
            HashSet<GridPosition> zoneBefore = scene.Reachability.Zone.ToHashSet();
            bool reachable = scene.Reachability.TryGetPath(SecondDestination, out PlannedPath? path);
            Check(reachable, "(2,2) est dans la zone du moteur après le 1er ordre");
            Click(scene, PrototypeScene.CellCenter(SecondDestination));
            await Settle("ordre-2-2");
            Check(reachable && scene.State.Position == SecondDestination
                && scene.State.Tu == beforeRefusals.Tu - path!.Tu && scene.State.Energy == beforeRefusals.Energy - path.Energy,
                $"2e ordre vers (2,2), débité du coût du chemin du moteur : {Describe(scene.State)}");
            HashSet<GridPosition> zoneAfter = scene.Reachability.Zone.ToHashSet();
            Check(!zoneAfter.SetEquals(zoneBefore) && zoneAfter.SetEquals(model.ComputeReachability(scene.State).Zone),
                $"zone recalculée depuis le nouvel état ({zoneBefore.Count} puis {zoneAfter.Count} cases)");
            CheckHud("après le 2e ordre");

            // Touche R : retour à l'état initial du scénario.
            PressKey(scene, Key.R);
            await Settle("touche-r");
            Check(scene.State == initial && scene.Reachability.Zone.ToHashSet().SetEquals(initialZone),
                $"touche R : état initial restitué ({Describe(scene.State)})");
            CheckHud("après la touche R");
        }
        catch (Exception exception)
        {
            GD.PrintErr($"SMOKE EXCEPTION : {exception}");
            scene.GetTree().Quit(2);
            return;
        }

        GD.Print(failures == 0 ? "SMOKE : RÉUSSITE" : $"SMOKE : ÉCHEC ({failures} contrôle(s))");
        scene.GetTree().Quit(failures == 0 ? 0 : 1);
    }

    private static bool Same(UnitState state, GridPosition position, Direction orientation, int tu, int energy) =>
        state.Position == position && state.Orientation == orientation && state.Tu == tu && state.Energy == energy;

    private static string Describe(UnitState state) =>
        $"{state.Position}, {state.Orientation}, {state.Tu} TU, {state.Energy} d'énergie";

    private static void Click(PrototypeScene scene, Vector2 position)
    {
        foreach (bool pressed in new[] { true, false })
        {
            scene.GetViewport().PushInput(new InputEventMouseButton
            {
                ButtonIndex = MouseButton.Left,
                Pressed = pressed,
                Position = position,
                GlobalPosition = position,
            });
        }
    }

    private static void PressKey(PrototypeScene scene, Key key)
    {
        foreach (bool pressed in new[] { true, false })
        {
            scene.GetViewport().PushInput(new InputEventKey { Keycode = key, Pressed = pressed });
        }
    }
}
