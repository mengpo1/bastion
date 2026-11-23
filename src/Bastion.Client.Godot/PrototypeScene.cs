using Bastion.Simulation.Movement;
using Godot;

namespace Bastion.Client;

/// <summary>
/// Scène unique du prototype technique (lots 1D à 1F) : une carte MEC-0003 de 5 × 5 cases et une unité, vues du dessus.
/// Trois scénarios fixes de démonstration (lot 1F) se chargent par les touches 1, 2 et 3 ; ce sont des données, et non
/// des règles de jeu. Toutes les règles (zone atteignable, chemins, coûts, collisions, rotations) viennent de
/// Bastion.Simulation : la scène convertit les coordonnées entre pixels et cases, transmet les ordres au moteur et
/// affiche ses résultats.
/// </summary>
public partial class PrototypeScene : Node2D
{
    private const int Columns = 5;
    private const int Rows = 5;
    private const decimal CellWidthMm = 1500m;
    private const float CellPixels = 96f;
    private static readonly Vector2 GridOrigin = new(24f, 24f);
    private static readonly GridPosition StartPosition = new(1, 4);
    private const Direction StartOrientation = Direction.N;
    private const int StartTu = 20;
    private const int StartEnergy = 10;
    private const string NoPath = "aucun";

    /// <summary>Titres des scénarios, dans l'ordre des touches 1, 2 et 3.</summary>
    private static readonly string[] ScenarioTitles = ["référence (lot 1D)", "mur et recherche de chemin", "coûts des terrains"];

    private static readonly Color FloorColor = new(0.82f, 0.82f, 0.78f);
    private static readonly Color ReachableColor = new(0.62f, 0.85f, 0.62f);
    private static readonly Color BlockedColor = new(0.25f, 0.25f, 0.28f);
    private static readonly Color LineColor = new(0.35f, 0.35f, 0.35f);
    private static readonly Color UnitColor = new(0.15f, 0.35f, 0.80f);
    private static readonly Color HeadingColor = new(0.95f, 0.85f, 0.20f);
    private static readonly Color WallColor = new(0.08f, 0.08f, 0.08f);
    private static readonly Color DifficultColor = new(0.93f, 0.60f, 0.13f);
    private static readonly Color VeryDifficultColor = new(0.50f, 0.27f, 0.10f);
    private const float TerrainFrame = 10f;

    private Label _hud = null!;

    /// <summary>Numéro du scénario chargé : 1, 2 ou 3.</summary>
    internal int Scenario { get; private set; }

    /// <summary>Moteur de la marche, construit pour la carte du scénario chargé.</summary>
    internal MovementModel Model { get; private set; } = null!;

    /// <summary>État courant de l'unité, tel que le moteur l'a rendu.</summary>
    internal UnitState State { get; private set; } = null!;

    /// <summary>Zone atteignable de l'état courant, calculée par le moteur.</summary>
    internal Reachability Reachability { get; private set; } = null!;

    /// <summary>Dernier résultat affiché.</summary>
    internal string LastResult { get; private set; } = string.Empty;

    /// <summary>Directions du chemin choisi par le moteur pour le dernier ordre exécuté, ou « aucun ».</summary>
    internal string LastPath { get; private set; } = NoPath;

    /// <summary>Texte du panneau d'information.</summary>
    internal string HudText => _hud.Text;

    public override void _Ready()
    {
        bool smokeTest = OS.GetCmdlineUserArgs().Contains("--smoke-test");
        try
        {
            _hud = GetNode<Label>("Hud");
            LoadScenario(1, "Scénario initialisé.");
        }
        catch (Exception exception) when (smokeTest)
        {
            // En contrôle fumée, un échec d'initialisation doit terminer le processus avec un code non nul.
            GD.PrintErr($"SMOKE EXCEPTION à l'initialisation de la scène : {exception}");
            GetTree().Quit(2);
            return;
        }

        if (smokeTest)
        {
            _ = SmokeTest.RunAsync(this);
        }
    }

    public override void _UnhandledInput(InputEvent @event)
    {
        if (@event is InputEventMouseButton { ButtonIndex: MouseButton.Left, Pressed: true } click)
        {
            OrderTo(CellAt(click.Position));
        }
        else if (@event is InputEventKey { Pressed: true, Echo: false } key)
        {
            if (key.Keycode == Key.R)
            {
                // Commande de débogage, et non règle de gameplay : recrée l'état initial du scénario.
                ResetScenario("Scénario réinitialisé (touche R).");
            }
            else if (ScenarioKey(key) is int scenario)
            {
                LoadScenario(scenario, $"Scénario {scenario} chargé (touche {scenario}).");
            }
        }
    }

    public override void _Draw()
    {
        TacticalMap map = Model.Map;
        for (int row = 0; row < Rows; row++)
        {
            for (int column = 0; column < Columns; column++)
            {
                var cell = new GridPosition(column, row);
                var rect = new Rect2(GridOrigin + new Vector2(column, row) * CellPixels, CellPixels, CellPixels);
                Color fill = map.IsBlocked(cell) ? BlockedColor
                    : Reachability.Contains(cell) ? ReachableColor
                    : FloorColor;
                DrawRect(rect, fill);
                if (TerrainColor(map.TerrainAt(cell)) is Color terrain)
                {
                    DrawRect(rect.Grow(-TerrainFrame / 2f), terrain, filled: false, width: TerrainFrame);
                }

                DrawRect(rect, LineColor, filled: false, width: 1f);
                if (map.IsBlocked(cell))
                {
                    DrawLine(rect.Position, rect.End, FloorColor, 2f);
                    DrawLine(new Vector2(rect.End.X, rect.Position.Y), new Vector2(rect.Position.X, rect.End.Y), FloorColor, 2f);
                }
            }
        }

        // Murs : lus sur les arêtes est et sud de chaque case, tracés à l'épaisseur donnée par le moteur.
        for (int row = 0; row < Rows; row++)
        {
            for (int column = 0; column < Columns; column++)
            {
                var cell = new GridPosition(column, row);
                Vector2 corner = GridOrigin + new Vector2(column, row) * CellPixels;
                if (column + 1 < Columns && map.WallBetween(cell, Direction.E) is WallType east)
                {
                    DrawLine(corner + new Vector2(CellPixels, 0f), corner + new Vector2(CellPixels, CellPixels), WallColor, WallPixels(east));
                }

                if (row + 1 < Rows && map.WallBetween(cell, Direction.S) is WallType south)
                {
                    DrawLine(corner + new Vector2(0f, CellPixels), corner + new Vector2(CellPixels, CellPixels), WallColor, WallPixels(south));
                }
            }
        }

        // Unité : disque de la largeur de son emprise, à l'échelle de la case ; trait vers son orientation.
        Vector2 center = CellCenter(State.Position);
        float radius = Model.Body.WidthMm / (float)map.CellWidthMm * CellPixels / 2f;
        (int columns, int rows) = State.Orientation.Offset();
        Vector2 heading = new Vector2(columns, rows).Normalized();
        DrawCircle(center, radius, UnitColor);
        DrawLine(center, center + heading * radius * 1.8f, HeadingColor, 4f);

        DrawLegend();
    }

    /// <summary>Centre, en pixels, d'une case de la carte.</summary>
    internal static Vector2 CellCenter(GridPosition cell) =>
        GridOrigin + (new Vector2(cell.Column, cell.Row) + new Vector2(0.5f, 0.5f)) * CellPixels;

    private static GridPosition CellAt(Vector2 position)
    {
        Vector2 local = (position - GridOrigin) / CellPixels;
        return new GridPosition(Mathf.FloorToInt(local.X), Mathf.FloorToInt(local.Y));
    }

    /// <summary>
    /// Carte d'un scénario de démonstration (lot 1F). Ce sont des données fixes, et non des règles de jeu.
    /// </summary>
    private static TacticalMap BuildMap(int scenario)
    {
        var map = new TacticalMapBuilder(Columns, Rows, CellWidthMm);
        TacticalMapBuilder layout = scenario switch
        {
            1 => map.Block(new GridPosition(3, 2)),
            2 => map.AddWall(new GridPosition(1, 4), Direction.E, WallType.Standard),
            3 => map.SetTerrain(new GridPosition(2, 4), TerrainType.Difficult).SetTerrain(new GridPosition(3, 4), TerrainType.VeryDifficult),
            _ => throw new ArgumentOutOfRangeException(nameof(scenario), scenario, "Scénario inconnu : 1, 2 ou 3 attendu."),
        };
        return layout.Build();
    }

    /// <summary>
    /// Scénario d'une touche 1, 2 ou 3 de la rangée des chiffres, reconnue par son libellé (clavier QWERTY) ou par sa
    /// position (clavier AZERTY, où ces touches donnent « & », « é » et « " » sans la touche Maj) ; sinon <c>null</c>.
    /// </summary>
    private static int? ScenarioKey(InputEventKey key)
    {
        for (int scenario = 1; scenario <= ScenarioTitles.Length; scenario++)
        {
            Key digit = Key.Key0 + scenario;
            if (key.Keycode == digit || key.PhysicalKeycode == digit)
            {
                return scenario;
            }
        }

        return null;
    }

    /// <summary>Couleur du cadre d'un terrain : aucune pour le terrain normal.</summary>
    private static Color? TerrainColor(TerrainType terrain) =>
        terrain == TerrainType.Difficult ? DifficultColor
        : terrain == TerrainType.VeryDifficult ? VeryDifficultColor
        : null;

    private static float WallPixels(WallType wall) => wall.ThicknessMm / (float)CellWidthMm * CellPixels;

    /// <summary>Légende sous la carte : zone, cases, murs et terrains, avec les noms de terrain du moteur.</summary>
    private void DrawLegend()
    {
        Font font = ThemeDB.FallbackFont;
        const int FontSize = 14;
        const float SwatchSize = 16f;
        var entries = new (string Text, Action<Rect2> Swatch)[]
        {
            ("zone atteignable", rect => DrawRect(rect, ReachableColor)),
            ("hors de la zone", rect => DrawRect(rect, FloorColor)),
            ("case infranchissable", rect =>
            {
                DrawRect(rect, BlockedColor);
                DrawLine(rect.Position, rect.End, FloorColor, 1f);
            }),
            ("mur", rect => DrawRect(new Rect2(rect.Position + new Vector2(0f, SwatchSize / 2f - 3f), SwatchSize, 6f), WallColor)),
            ($"terrain {TerrainType.Difficult.Name}", rect =>
            {
                DrawRect(rect, FloorColor);
                DrawRect(rect.Grow(-2f), DifficultColor, filled: false, width: 4f);
            }),
            ($"terrain {TerrainType.VeryDifficult.Name}", rect =>
            {
                DrawRect(rect, FloorColor);
                DrawRect(rect.Grow(-2f), VeryDifficultColor, filled: false, width: 4f);
            }),
        };

        float top = GridOrigin.Y + Rows * CellPixels + 12f;
        for (int index = 0; index < entries.Length; index++)
        {
            var position = new Vector2(GridOrigin.X + index % 2 * 240f, top + index / 2 * 22f);
            entries[index].Swatch(new Rect2(position, SwatchSize, SwatchSize));
            DrawString(font, position + new Vector2(SwatchSize + 8f, 13f), entries[index].Text, fontSize: FontSize);
        }

        DrawString(font, new Vector2(GridOrigin.X, top + 3 * 22f + 13f), $"Sans cadre : terrain {TerrainType.Normal.Name}.", fontSize: FontSize);
    }

    /// <summary>Transmet un ordre de déplacement au moteur et affiche l'état qu'il rend.</summary>
    private void OrderTo(GridPosition destination)
    {
        if (!Model.Map.Contains(destination))
        {
            LastResult = "Clic hors de la carte : aucun ordre transmis.";
            Refresh();
            return;
        }

        OrderOutcome outcome = Model.ExecuteOrder(State, destination);
        State = outcome.FinalState;
        LastResult = outcome.Message;
        if (outcome.Path is not null)
        {
            LastPath = string.Join(" → ", outcome.Path.Steps);
        }

        Refresh();
    }

    /// <summary>Charge la carte d'un scénario et place l'unité dans son état initial.</summary>
    private void LoadScenario(int scenario, string message)
    {
        Model = new MovementModel(BuildMap(scenario), MovementRules.Initial, UnitBody.StandardHuman);
        Scenario = scenario;
        ResetScenario(message);
    }

    private void ResetScenario(string message)
    {
        State = Model.CreateState(StartPosition, StartOrientation, StartTu, StartEnergy);
        LastResult = message;
        LastPath = NoPath;
        Refresh();
    }

    /// <summary>Recalcule la zone à partir de l'état courant, puis met à jour le texte et le dessin.</summary>
    private void Refresh()
    {
        Reachability = Model.ComputeReachability(State);
        _hud.Text =
            "Bastion — banc d'essai de MEC-0003 (lots 1D à 1F)\n" +
            $"Scénario {Scenario} : {ScenarioTitles[Scenario - 1]}\n\n" +
            $"Position : {State.Position}\n" +
            $"Orientation : {State.Orientation}\n" +
            $"TU restantes : {State.Tu}\n" +
            $"Énergie restante : {State.Energy}\n" +
            $"Cases atteignables : {Reachability.Zone.Count}\n" +
            $"Chemin du dernier ordre exécuté : {LastPath}\n\n" +
            $"Dernier résultat : {LastResult}\n\n" +
            "1, 2, 3 : choisir le scénario\n" +
            "Clic gauche : ordre de déplacement\n" +
            "R : réinitialiser le scénario (débogage)";
        QueueRedraw();
    }
}
