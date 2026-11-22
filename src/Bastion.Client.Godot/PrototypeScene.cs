using Bastion.Simulation.Movement;
using Godot;

namespace Bastion.Client;

/// <summary>
/// Scène unique du prototype technique (lot 1D) : une carte MEC-0003 de 5 × 5 cases et une unité, vues du dessus.
/// Toutes les règles (zone atteignable, chemins, coûts, collisions) viennent de Bastion.Simulation : la scène
/// convertit les coordonnées entre pixels et cases, transmet les ordres au moteur et affiche ses résultats.
/// </summary>
public partial class PrototypeScene : Node2D
{
    private const int Columns = 5;
    private const int Rows = 5;
    private const decimal CellWidthMm = 1500m;
    private const float CellPixels = 96f;
    private static readonly Vector2 GridOrigin = new(24f, 24f);
    private static readonly GridPosition BlockedCell = new(3, 2);
    private static readonly GridPosition StartPosition = new(1, 4);
    private const Direction StartOrientation = Direction.N;
    private const int StartTu = 20;
    private const int StartEnergy = 10;

    private static readonly Color FloorColor = new(0.82f, 0.82f, 0.78f);
    private static readonly Color ReachableColor = new(0.62f, 0.85f, 0.62f);
    private static readonly Color BlockedColor = new(0.25f, 0.25f, 0.28f);
    private static readonly Color LineColor = new(0.35f, 0.35f, 0.35f);
    private static readonly Color UnitColor = new(0.15f, 0.35f, 0.80f);
    private static readonly Color HeadingColor = new(0.95f, 0.85f, 0.20f);

    private TacticalMap _map = null!;
    private Label _hud = null!;

    /// <summary>Moteur de la marche, construit une fois pour la carte du scénario.</summary>
    internal MovementModel Model { get; private set; } = null!;

    /// <summary>État courant de l'unité, tel que le moteur l'a rendu.</summary>
    internal UnitState State { get; private set; } = null!;

    /// <summary>Zone atteignable de l'état courant, calculée par le moteur.</summary>
    internal Reachability Reachability { get; private set; } = null!;

    /// <summary>Dernier résultat affiché.</summary>
    internal string LastResult { get; private set; } = string.Empty;

    /// <summary>Texte du panneau d'information.</summary>
    internal string HudText => _hud.Text;

    public override void _Ready()
    {
        bool smokeTest = OS.GetCmdlineUserArgs().Contains("--smoke-test");
        try
        {
            _hud = GetNode<Label>("Hud");
            _map = new TacticalMapBuilder(Columns, Rows, CellWidthMm).Block(BlockedCell).Build();
            Model = new MovementModel(_map, MovementRules.Initial, UnitBody.StandardHuman);
            ResetScenario("Scénario initialisé.");
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
        else if (@event is InputEventKey { Keycode: Key.R, Pressed: true, Echo: false })
        {
            // Commande de débogage, et non règle de gameplay : recrée l'état initial du scénario.
            ResetScenario("Scénario réinitialisé (touche R).");
        }
    }

    public override void _Draw()
    {
        for (int row = 0; row < Rows; row++)
        {
            for (int column = 0; column < Columns; column++)
            {
                var cell = new GridPosition(column, row);
                var rect = new Rect2(GridOrigin + new Vector2(column, row) * CellPixels, CellPixels, CellPixels);
                Color fill = _map.IsBlocked(cell) ? BlockedColor
                    : Reachability.Contains(cell) ? ReachableColor
                    : FloorColor;
                DrawRect(rect, fill);
                DrawRect(rect, LineColor, filled: false, width: 1f);
                if (_map.IsBlocked(cell))
                {
                    DrawLine(rect.Position, rect.End, FloorColor, 2f);
                    DrawLine(new Vector2(rect.End.X, rect.Position.Y), new Vector2(rect.Position.X, rect.End.Y), FloorColor, 2f);
                }
            }
        }

        // Unité : disque de la largeur de son emprise, à l'échelle de la case ; trait vers son orientation.
        Vector2 center = CellCenter(State.Position);
        float radius = Model.Body.WidthMm / (float)_map.CellWidthMm * CellPixels / 2f;
        (int columns, int rows) = State.Orientation.Offset();
        Vector2 heading = new Vector2(columns, rows).Normalized();
        DrawCircle(center, radius, UnitColor);
        DrawLine(center, center + heading * radius * 1.8f, HeadingColor, 4f);
    }

    /// <summary>Centre, en pixels, d'une case de la carte.</summary>
    internal static Vector2 CellCenter(GridPosition cell) =>
        GridOrigin + (new Vector2(cell.Column, cell.Row) + new Vector2(0.5f, 0.5f)) * CellPixels;

    private static GridPosition CellAt(Vector2 position)
    {
        Vector2 local = (position - GridOrigin) / CellPixels;
        return new GridPosition(Mathf.FloorToInt(local.X), Mathf.FloorToInt(local.Y));
    }

    /// <summary>Transmet un ordre de déplacement au moteur et affiche l'état qu'il rend.</summary>
    private void OrderTo(GridPosition destination)
    {
        if (!_map.Contains(destination))
        {
            LastResult = "Clic hors de la carte : aucun ordre transmis.";
            Refresh();
            return;
        }

        OrderOutcome outcome = Model.ExecuteOrder(State, destination);
        State = outcome.FinalState;
        LastResult = outcome.Message;
        Refresh();
    }

    private void ResetScenario(string message)
    {
        State = Model.CreateState(StartPosition, StartOrientation, StartTu, StartEnergy);
        LastResult = message;
        Refresh();
    }

    /// <summary>Recalcule la zone à partir de l'état courant, puis met à jour le texte et le dessin.</summary>
    private void Refresh()
    {
        Reachability = Model.ComputeReachability(State);
        _hud.Text =
            "Bastion — prototype technique (lot 1D)\n\n" +
            $"Position : {State.Position}\n" +
            $"Orientation : {State.Orientation}\n" +
            $"TU restantes : {State.Tu}\n" +
            $"Énergie restante : {State.Energy}\n" +
            $"Cases atteignables : {Reachability.Zone.Count}\n\n" +
            $"Dernier résultat : {LastResult}\n\n" +
            "Clic gauche : ordre de déplacement\n" +
            "R : réinitialiser (débogage)";
        QueueRedraw();
    }
}
