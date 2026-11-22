namespace Bastion.Simulation.Movement.Geometry;

/// <summary>
/// Contrôle physique, en plan, du volume réel de l'unité (A1, A2, A5, A8) contre les obstacles de la
/// carte : murs, cases infranchissables et bords. Repère : origine au centre de la case (0, 0), x vers
/// l'est, y vers le sud ; le centre de la case (c, l) est en (c × largeur, l × largeur).
/// </summary>
internal sealed class StepGeometry
{
    private readonly int _cellWidth;
    private readonly Rational _halfWidth;
    private readonly Rational _halfDepth;
    private readonly Rational _radiusSquared;
    private readonly List<Box> _obstacles;

    public StepGeometry(TacticalMap map, UnitBody body)
    {
        _cellWidth = map.CellWidthMm;
        _halfWidth = Rational.Of(body.WidthMm, 2);
        _halfDepth = Rational.Of(body.DepthMm, 2);
        _radiusSquared = _halfWidth * _halfWidth + _halfDepth * _halfDepth;
        _obstacles = BuildObstacles(map, body);
    }

    /// <summary>Emprise au repos, centrée sur sa case (A1) : libre de tout chevauchement ?</summary>
    public bool RestIsFree(GridPosition cell, Direction heading)
    {
        (Rational x, Rational y) = Center(cell);
        Vec[] corners = Corners(new Vec(x, y), heading);
        return Near(x, x, y, y).All(box => !Collision.ConvexOverlapsBox(corners, Axes(heading), box));
    }

    /// <summary>
    /// Rotation au centre de la case, de <paramref name="from"/> à <paramref name="to"/>, dans le sens
    /// donné : la surface balayée par l'emprise rectangulaire réelle (A5, A7) est-elle libre ?
    /// </summary>
    /// <remarks>
    /// La rotation est décomposée en huitièmes de tour. Pendant un huitième de tour, la surface balayée
    /// est l'union exacte des deux emprises extrêmes et des quatre secteurs parcourus par les coins.
    /// </remarks>
    public bool RotationIsFree(GridPosition cell, Direction from, Direction to, RotationSense sense)
    {
        (Rational x, Rational y) = Center(cell);
        var center = new Vec(x, y);
        List<Box> near = Near(x, x, y, y).ToList();
        int step = sense == RotationSense.Clockwise ? 1 : -1;
        var heading = from;
        while (heading != to)
        {
            var next = (Direction)(((int)heading + step + 8) % 8);
            if (!EighthTurnIsFree(center, heading, next, near))
            {
                return false;
            }

            heading = next;
        }

        return true;
    }

    /// <summary>
    /// Translation rectiligne du centre, de la case <paramref name="from"/> à la case <paramref name="to"/>
    /// voisine orthogonale, l'unité restant orientée selon <paramref name="heading"/> : le volume réel
    /// balayé est-il libre ? Le volume balayé est l'enveloppe convexe des deux emprises extrêmes.
    /// </summary>
    public bool TranslationIsFree(GridPosition from, GridPosition to, Direction heading)
    {
        (Rational x0, Rational y0) = Center(from);
        (Rational x1, Rational y1) = Center(to);
        Vec[] start = Corners(new Vec(x0, y0), heading);
        Vec[] end = Corners(new Vec(x1, y1), heading);
        Vec[] hull = [.. start, .. end];
        IEnumerable<Box> near = Near(Min(x0, x1), Max(x0, x1), Min(y0, y1), Max(y0, y1));
        return near.All(box => !Collision.ConvexOverlapsBox(hull, Axes(heading), box));
    }

    private bool EighthTurnIsFree(Vec center, Direction from, Direction to, List<Box> near)
    {
        Vec[] startOffsets = Offsets(from);
        Vec[] endOffsets = Offsets(to);
        Vec[] startCorners = startOffsets.Select(offset => center + offset).ToArray();
        Vec[] endCorners = endOffsets.Select(offset => center + offset).ToArray();
        foreach (Box box in near)
        {
            if (Collision.ConvexOverlapsBox(startCorners, Axes(from), box)
                || Collision.ConvexOverlapsBox(endCorners, Axes(to), box))
            {
                return false;
            }

            for (int corner = 0; corner < 4; corner++)
            {
                if (Collision.SectorOverlapsBox(center, startOffsets[corner], endOffsets[corner], _radiusSquared, box))
                {
                    return false;
                }
            }
        }

        return true;
    }

    private (Rational X, Rational Y) Center(GridPosition cell) =>
        ((long)cell.Column * _cellWidth, (long)cell.Row * _cellWidth);

    /// <summary>
    /// Obstacles qui peuvent être atteints : tout point de l'unité reste à une distance au plus égale
    /// à sa demi-diagonale d'un point du trajet de son centre, ici inclus dans le pavé indiqué.
    /// </summary>
    private IEnumerable<Box> Near(Rational minX, Rational maxX, Rational minY, Rational maxY) =>
        _obstacles.Where(box =>
            !BeyondReach(box.MinX - maxX)
            && !BeyondReach(minX - box.MaxX)
            && !BeyondReach(box.MinY - maxY)
            && !BeyondReach(minY - box.MaxY));

    private bool BeyondReach(Rational gap) => gap.Sign > 0 && (gap * gap).CompareTo(_radiusSquared) >= 0;

    /// <summary>
    /// Vecteurs du centre vers les quatre coins de l'emprise orientée. Les coins gardent le même rang
    /// d'une orientation à l'autre : un coin j décrit un arc pendant une rotation.
    /// </summary>
    private Vec[] Offsets(Direction heading)
    {
        (Vec forward, Vec right) = Frame(heading);
        Surd halfWidth = _halfWidth;
        Surd halfDepth = _halfDepth;
        Vec lateral = right * halfWidth;
        Vec longitudinal = forward * halfDepth;
        return
        [
            lateral + longitudinal,
            lateral - longitudinal,
            Zero - lateral - longitudinal,
            Zero - lateral + longitudinal,
        ];
    }

    private Vec[] Corners(Vec center, Direction heading) =>
        Offsets(heading).Select(offset => center + offset).ToArray();

    /// <summary>Normales des côtés de l'emprise orientée : sa direction de face et sa direction latérale.</summary>
    private static Vec[] Axes(Direction heading)
    {
        (Vec forward, Vec right) = Frame(heading);
        return [forward, right];
    }

    private static readonly Vec Zero = new(Surd.Zero, Surd.Zero);

    /// <summary>
    /// Vecteur de face et vecteur latéral droit de l'orientation (A8 : la profondeur suit la face,
    /// la largeur lui est perpendiculaire). Cap θ = rang × 45°, compté du nord dans le sens horaire :
    /// face = (sin θ, −cos θ), droite = (cos θ, sin θ).
    /// </summary>
    private static (Vec Forward, Vec Right) Frame(Direction heading)
    {
        Surd h = Surd.HalfRoot2;
        (Surd sin, Surd cos) = heading switch
        {
            Direction.N => ((Surd)0, (Surd)1),
            Direction.NE => (h, h),
            Direction.E => ((Surd)1, (Surd)0),
            Direction.SE => (h, -h),
            Direction.S => ((Surd)0, (Surd)(-1)),
            Direction.SW => (-h, -h),
            Direction.W => ((Surd)(-1), (Surd)0),
            Direction.NW => (-h, h),
            _ => throw new ArgumentOutOfRangeException(nameof(heading), heading, "Orientation inconnue."),
        };
        return (new Vec(sin, -cos), new Vec(cos, sin));
    }

    private static List<Box> BuildObstacles(TacticalMap map, UnitBody body)
    {
        int width = map.CellWidthMm;
        Rational half = Rational.Of(width, 2);
        var obstacles = new List<Box>();
        for (int column = 0; column < map.Columns; column++)
        {
            for (int row = 0; row < map.Rows; row++)
            {
                if (map.IsBlocked(new GridPosition(column, row)))
                {
                    Rational x = (long)column * width;
                    Rational y = (long)row * width;
                    obstacles.Add(new Box(x - half, y - half, x + half, y + half));
                }
            }
        }

        foreach ((WallEdge edge, WallType wall) in map.Walls)
        {
            Rational x = (long)edge.Cell.Column * width;
            Rational y = (long)edge.Cell.Row * width;
            Rational halfThickness = Rational.Of(wall.ThicknessMm, 2);
            obstacles.Add(edge.IsEastEdge
                ? new Box(x + half - halfThickness, y - half, x + half + halfThickness, y + half)
                : new Box(x - half, y + half - halfThickness, x + half, y + half + halfThickness));
        }

        // Bords de la carte : quatre pavés extérieurs, assez larges pour toute partie de l'unité.
        Rational margin = (long)body.WidthMm + body.DepthMm + width;
        Rational minX = -half;
        Rational minY = -half;
        Rational maxX = (long)(map.Columns - 1) * width + half;
        Rational maxY = (long)(map.Rows - 1) * width + half;
        obstacles.Add(new Box(minX - margin, minY - margin, minX, maxY + margin));
        obstacles.Add(new Box(maxX, minY - margin, maxX + margin, maxY + margin));
        obstacles.Add(new Box(minX - margin, minY - margin, maxX + margin, minY));
        obstacles.Add(new Box(minX - margin, maxY, maxX + margin, maxY + margin));
        return obstacles;
    }

    private static Rational Min(Rational a, Rational b) => a.CompareTo(b) <= 0 ? a : b;

    private static Rational Max(Rational a, Rational b) => a.CompareTo(b) >= 0 ? a : b;
}
