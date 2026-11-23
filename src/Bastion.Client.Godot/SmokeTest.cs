using Bastion.Simulation.Movement;
using Godot;

namespace Bastion.Client;

/// <summary>
/// Contrôle fumée du prototype (lots 1D et 1F), lancé par l'argument utilisateur « --smoke-test ». Il parcourt le
/// scénario 1 (contrôles du lot 1D, inchangés), puis les scénarios 2 et 3 du lot 1F, chargés par les touches 2 et 3,
/// et revient au scénario 1 par la touche 1.
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

            // Le chemin attendu est fourni par l'appelant (moteur ou « aucun »), jamais relu dans la scène.
            void CheckScenario(int number, string expectedPath, string when)
            {
                CheckHud(when);
                Check(scene.Scenario == number && scene.LastPath == expectedPath
                    && scene.HudText.Contains($"Scénario {number} : ", StringComparison.Ordinal)
                    && scene.HudText.Contains($"Chemin du dernier ordre exécuté : {expectedPath}\n", StringComparison.Ordinal),
                    $"panneau : scénario {number}, chemin « {expectedPath} » attendu {when} "
                    + $"(LastPath : « {scene.LastPath} » ; panneau : « {PathLine(scene.HudText)} »)");
            }

            static string PathText(OrderOutcome order) => order.Path is { } path ? string.Join(" → ", path.Steps) : "(ordre refusé)";
            static string PathLine(string hud) =>
                hud.Split('\n').FirstOrDefault(line => line.StartsWith("Chemin du dernier ordre exécuté : ", StringComparison.Ordinal))
                ?? "(ligne absente)";

            // Lot 1F : un ordre exécuté dans le scénario 1 affiche son chemin ; le changement de scénario devra l'effacer.
            OrderOutcome expectedReferencePath = model.ExecuteOrder(initial, FirstDestination);
            Click(scene, PrototypeScene.CellCenter(FirstDestination));
            await Settle("s1-chemin");
            CheckScenario(1, PathText(expectedReferencePath), "après un ordre vers (2,4)");

            // Scénario 2 (lot 1F) : un mur standard sur l'arête est de (1,4). Touche 2 donnée par son seul libellé, sans
            // position : la reconnaissance par libellé est ainsi contrôlée à part de la reconnaissance par position.
            PressKey(scene, Key.Key2, Key.None);
            await Settle("scenario-2");
            MovementModel wallModel = scene.Model;
            UnitState wallStart = scene.State;
            Check(scene.Scenario == 2 && Same(wallStart, new GridPosition(1, 4), Direction.N, 20, 10) && scene.LastPath == "aucun",
                $"touche 2 : scénario 2 chargé, état initial {Describe(wallStart)}");
            Check(Layout(wallModel.Map) == "murs : (1,4) E standard ; cases infranchissables : aucune ; terrains non normaux : aucun"
                && wallModel.Map.Columns == 5 && wallModel.Map.Rows == 5 && wallModel.Map.CellWidthMm == 1500
                && wallModel.Body == UnitBody.StandardHuman,
                $"carte du scénario 2 : {wallModel.Map.Columns} × {wallModel.Map.Rows} cases de {wallModel.Map.CellWidthMm} mm, {Layout(wallModel.Map)}");
            HashSet<GridPosition> wallZone = scene.Reachability.Zone.ToHashSet();
            Check(wallZone.SetEquals(wallModel.ComputeReachability(wallStart).Zone), $"zone affichée = zone du moteur ({wallZone.Count} cases)");
            CheckScenario(2, "aucun", "au chargement du scénario 2");

            // Le pas direct est interdit par le mur ; la case située derrière reste atteignable par un autre chemin.
            StepOutcome direct = wallModel.EvaluateStep(wallStart, Direction.E);
            Check(direct.Refusal == StepRefusal.WallOnEdge, $"pas direct E depuis (1,4) refusé par le moteur : {direct.Message}");
            bool detourFound = scene.Reachability.TryGetPath(FirstDestination, out PlannedPath? detour);
            Check(detourFound && !detour!.Steps.SequenceEqual([Direction.E]),
                $"(2,4) reste dans la zone du moteur, par un autre chemin que le pas direct : {(detourFound ? string.Join(" → ", detour!.Steps) : "aucun")}");
            OrderOutcome expectedDetour = wallModel.ExecuteOrder(wallStart, FirstDestination);
            Click(scene, PrototypeScene.CellCenter(FirstDestination));
            await Settle("s2-ordre-2-4");
            Check(expectedDetour.Path is not null && scene.State == expectedDetour.FinalState && scene.LastResult == expectedDetour.Message
                && scene.LastPath == string.Join(" → ", expectedDetour.Path.Steps) && scene.State.Position == FirstDestination,
                $"clic sur (2,4) = résultat d'ExecuteOrder : {Describe(scene.State)}, chemin {scene.LastPath} ({scene.LastResult})");
            CheckScenario(2, PathText(expectedDetour), "après l'ordre vers (2,4)");

            // Un ordre refusé n'est pas exécuté : le chemin affiché reste celui du dernier ordre exécuté.
            UnitState afterDetour = scene.State;
            OrderOutcome expectedRefusal = wallModel.ExecuteOrder(afterDetour, OutOfZone);
            Click(scene, PrototypeScene.CellCenter(OutOfZone));
            await Settle("s2-clic-hors-zone");
            Check(!expectedRefusal.InZone && scene.State == afterDetour && scene.LastResult == expectedRefusal.Message,
                $"clic sur (4,0), hors de la zone du moteur : état inchangé ({scene.LastResult})");
            CheckScenario(2, PathText(expectedDetour), "après l'ordre refusé");

            // Un second ordre exécuté, au chemin différent, remplace le chemin affiché : c'est celui du dernier ordre.
            var eastOfDetour = new GridPosition(3, 4);
            OrderOutcome expectedSecond = wallModel.ExecuteOrder(afterDetour, eastOfDetour);
            Click(scene, PrototypeScene.CellCenter(eastOfDetour));
            await Settle("s2-ordre-3-4");
            Check(expectedSecond.Path is not null && PathText(expectedSecond) != PathText(expectedDetour)
                && scene.State == expectedSecond.FinalState && scene.LastResult == expectedSecond.Message,
                $"second ordre vers (3,4) = résultat d'ExecuteOrder, au chemin différent du premier : {Describe(scene.State)}, chemin {PathText(expectedSecond)}");
            CheckScenario(2, PathText(expectedSecond), "après le second ordre");

            PressKey(scene, Key.R);
            await Settle("s2-touche-r");
            Check(scene.Scenario == 2 && scene.State == wallStart && scene.LastPath == "aucun"
                && scene.Reachability.Zone.ToHashSet().SetEquals(wallZone) && Layout(scene.Model.Map) == Layout(wallModel.Map),
                $"touche R : scénario 2 conservé, état initial restitué ({Describe(scene.State)})");
            CheckScenario(2, "aucun", "après la touche R");
            Click(scene, PrototypeScene.CellCenter(FirstDestination));
            await Settle("s2-ordre-2-4-bis");
            Check(scene.State == expectedDetour.FinalState, $"après R, clic sur (2,4) : même résultat ({Describe(scene.State)})");
            CheckScenario(2, PathText(expectedDetour), "après le nouvel ordre vers (2,4)");

            // Scénario 3 (lot 1F) : terrains difficile et très difficile. Touche 3 telle qu'un clavier AZERTY la donne,
            // sans la touche Maj : libellé « " », position de la touche 3.
            PressKey(scene, Key.Quotedbl, Key.Key3);
            await Settle("scenario-3");
            MovementModel terrainModel = scene.Model;
            UnitState terrainStart = scene.State;
            Check(scene.Scenario == 3 && Same(terrainStart, new GridPosition(1, 4), Direction.N, 20, 10),
                $"touche 3 : scénario 3 chargé, état initial {Describe(terrainStart)}");
            Check(Layout(terrainModel.Map) == "murs : aucun ; cases infranchissables : aucune ; terrains non normaux : (2,4) difficile, (3,4) très difficile"
                && terrainModel.Map.Columns == 5 && terrainModel.Map.Rows == 5 && terrainModel.Map.CellWidthMm == 1500
                && terrainModel.Body == UnitBody.StandardHuman,
                $"carte du scénario 3 : {terrainModel.Map.Columns} × {terrainModel.Map.Rows} cases de {terrainModel.Map.CellWidthMm} mm, {Layout(terrainModel.Map)}");
            Check(scene.Reachability.Zone.ToHashSet().SetEquals(terrainModel.ComputeReachability(terrainStart).Zone),
                $"zone affichée = zone du moteur ({scene.Reachability.Zone.Count} cases)");
            CheckScenario(3, "aucun", "au chargement du scénario 3");

            // Valeurs fixées par le mandat 1F, §2, et comparées au résultat réel d'ExecuteOrder.
            var difficult = new GridPosition(2, 4);
            var veryDifficult = new GridPosition(3, 4);
            OrderOutcome expectedDifficult = terrainModel.ExecuteOrder(terrainStart, difficult);
            Click(scene, PrototypeScene.CellCenter(difficult));
            await Settle("s3-ordre-2-4");
            Check(scene.State == expectedDifficult.FinalState && scene.LastResult == expectedDifficult.Message
                && scene.State.Position == difficult && scene.State.Tu == 14 && scene.State.Energy == 7,
                $"clic sur (2,4), terrain difficile = résultat d'ExecuteOrder, 14 TU et 7 d'énergie attendues : {Describe(scene.State)}");
            UnitState afterDifficult = scene.State;
            OrderOutcome expectedVeryDifficult = terrainModel.ExecuteOrder(afterDifficult, veryDifficult);
            Click(scene, PrototypeScene.CellCenter(veryDifficult));
            await Settle("s3-ordre-3-4");
            Check(scene.State == expectedVeryDifficult.FinalState && scene.LastResult == expectedVeryDifficult.Message
                && scene.State.Position == veryDifficult && scene.State.Tu == 6 && scene.State.Energy == 3,
                $"clic sur (3,4), terrain très difficile = résultat d'ExecuteOrder, 6 TU et 3 d'énergie attendues : {Describe(scene.State)}");
            CheckScenario(3, PathText(expectedVeryDifficult), "après les deux ordres");

            PressKey(scene, Key.R);
            await Settle("s3-touche-r");
            Check(scene.Scenario == 3 && scene.State == terrainStart && Layout(scene.Model.Map) == Layout(terrainModel.Map),
                $"touche R : scénario 3 conservé, état initial restitué ({Describe(scene.State)})");
            CheckScenario(3, "aucun", "après la touche R");
            Click(scene, PrototypeScene.CellCenter(difficult));
            await Settle("s3-ordre-2-4-bis");
            Check(scene.State == expectedDifficult.FinalState, $"après R, clic sur (2,4) : même résultat ({Describe(scene.State)})");
            CheckScenario(3, PathText(expectedDifficult), "après le nouvel ordre vers (2,4)");

            // Touches sans effet : la touche 1 du pavé numérique et la barre d'espace ne chargent aucun scénario.
            UnitState beforeOtherKeys = scene.State;
            string resultBeforeOtherKeys = scene.LastResult;
            PressKey(scene, Key.Kp1, Key.Kp1);
            PressKey(scene, Key.Space, Key.Space);
            await Settle("s3-touches-sans-effet");
            Check(scene.Scenario == 3 && scene.State == beforeOtherKeys && scene.LastResult == resultBeforeOtherKeys,
                $"touche 1 du pavé numérique et espace : aucun effet ({Describe(scene.State)})");
            CheckScenario(3, PathText(expectedDifficult), "après les touches sans effet");

            // Retour au scénario 1 depuis un état déplacé. Touche 1 telle qu'un clavier AZERTY la donne : « & », touche 1.
            PressKey(scene, Key.Ampersand, Key.Key1);
            await Settle("retour-scenario-1");
            Check(scene.Scenario == 1 && scene.State == initial && scene.Reachability.Zone.ToHashSet().SetEquals(initialZone)
                && Layout(scene.Model.Map) == "murs : aucun ; cases infranchissables : (3,2) ; terrains non normaux : aucun",
                $"touche 1 : scénario 1 rechargé dans son état initial ({Describe(scene.State)}, {Layout(scene.Model.Map)})");
            CheckScenario(1, "aucun", "après le retour au scénario 1");
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

    /// <summary>Touche donnée par son libellé et par sa position, comme le fait un clavier réel.</summary>
    private static void PressKey(PrototypeScene scene, Key keycode, Key physicalKeycode)
    {
        foreach (bool pressed in new[] { true, false })
        {
            scene.GetViewport().PushInput(new InputEventKey { Keycode = keycode, PhysicalKeycode = physicalKeycode, Pressed = pressed });
        }
    }

    /// <summary>Description d'une carte lue par les API publiques du moteur : taille, murs, cases infranchissables, terrains.</summary>
    private static string Layout(TacticalMap map)
    {
        var walls = new List<string>();
        var blocked = new List<string>();
        var terrains = new List<string>();
        for (int row = 0; row < map.Rows; row++)
        {
            for (int column = 0; column < map.Columns; column++)
            {
                var cell = new GridPosition(column, row);
                foreach (Direction side in new[] { Direction.E, Direction.S })
                {
                    if (map.Contains(cell.Step(side)) && map.WallBetween(cell, side) is WallType wall)
                    {
                        walls.Add($"{cell} {side} {wall.Name}");
                    }
                }

                if (map.IsBlocked(cell))
                {
                    blocked.Add($"{cell}");
                }

                if (map.TerrainAt(cell) != TerrainType.Normal)
                {
                    terrains.Add($"{cell} {map.TerrainAt(cell).Name}");
                }
            }
        }

        static string Join(List<string> items, string none) => items.Count == 0 ? none : string.Join(", ", items);
        return $"murs : {Join(walls, "aucun")} ; cases infranchissables : {Join(blocked, "aucune")} ; terrains non normaux : {Join(terrains, "aucun")}";
    }
}
