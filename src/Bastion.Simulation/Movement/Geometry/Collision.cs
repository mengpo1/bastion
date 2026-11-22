namespace Bastion.Simulation.Movement.Geometry;

/// <summary>
/// Tests exacts de chevauchement entre un volume balayé et un pavé d'obstacle.
/// Un chevauchement est une intersection des intérieurs : le simple contact n'en est pas un (Q4.2).
/// </summary>
internal static class Collision
{
    private static readonly Vec AxisX = new(1, 0);
    private static readonly Vec AxisY = new(0, 1);

    /// <summary>
    /// Chevauchement entre l'enveloppe convexe de <paramref name="points"/> et un pavé, par le théorème
    /// des axes séparateurs. <paramref name="polygonAxes"/> doit contenir les normales des arêtes de
    /// l'enveloppe qui ne sont pas parallèles aux axes ; les axes du pavé sont ajoutés ici.
    /// </summary>
    public static bool ConvexOverlapsBox(IReadOnlyList<Vec> points, IEnumerable<Vec> polygonAxes, Box box)
    {
        Vec[] corners = box.Corners();
        foreach (Vec axis in polygonAxes.Append(AxisX).Append(AxisY))
        {
            (Surd minPolygon, Surd maxPolygon) = Project(points, axis);
            (Surd minBox, Surd maxBox) = Project(corners, axis);
            if (maxPolygon.CompareTo(minBox) <= 0 || maxBox.CompareTo(minPolygon) <= 0)
            {
                return false;
            }
        }

        return true;
    }

    /// <summary>
    /// Chevauchement entre un secteur circulaire et un pavé. Le secteur a pour sommet
    /// <paramref name="center"/>, pour rayon la longueur commune de <paramref name="from"/> et de
    /// <paramref name="to"/> (carré <paramref name="radiusSquared"/>), et s'étend entre ces deux rayons,
    /// sous un angle inférieur à 180°.
    /// </summary>
    /// <remarks>
    /// Méthode : le pavé est découpé par le coin angulaire du secteur. Le chevauchement existe si et
    /// seulement si ce polygone découpé a une aire non nulle et s'approche du sommet à une distance
    /// strictement inférieure au rayon.
    /// </remarks>
    public static bool SectorOverlapsBox(Vec center, Vec from, Vec to, Rational radiusSquared, Box box)
    {
        List<Vec> polygon = box.Corners().Select(corner => corner - center).ToList();
        int orientation = from.Cross(to).Sign;
        polygon = ClipByHalfPlane(polygon, point => from.Cross(point) * orientation);
        polygon = ClipByHalfPlane(polygon, point => point.Cross(to) * orientation);
        if (polygon.Count < 3 || TwiceArea(polygon).Sign == 0)
        {
            return false;
        }

        return DistanceSquaredToOrigin(polygon).CompareTo(radiusSquared) < 0;
    }

    private static (Surd Min, Surd Max) Project(IReadOnlyList<Vec> points, Vec axis)
    {
        Surd min = points[0].Dot(axis);
        Surd max = min;
        for (int index = 1; index < points.Count; index++)
        {
            Surd value = points[index].Dot(axis);
            min = Surd.Min(min, value);
            max = Surd.Max(max, value);
        }

        return (min, max);
    }

    /// <summary>Conserve la partie du polygone convexe où la fonction linéaire est positive ou nulle.</summary>
    private static List<Vec> ClipByHalfPlane(List<Vec> polygon, Func<Vec, Surd> side)
    {
        var result = new List<Vec>();
        for (int index = 0; index < polygon.Count; index++)
        {
            Vec current = polygon[index];
            Vec next = polygon[(index + 1) % polygon.Count];
            Surd currentSide = side(current);
            Surd nextSide = side(next);
            if (currentSide.Sign >= 0)
            {
                result.Add(current);
            }

            if (currentSide.Sign * nextSide.Sign < 0)
            {
                Surd ratio = currentSide / (currentSide - nextSide);
                result.Add(current + (next - current) * ratio);
            }
        }

        return result;
    }

    private static Surd TwiceArea(IReadOnlyList<Vec> polygon)
    {
        Surd sum = Surd.Zero;
        for (int index = 0; index < polygon.Count; index++)
        {
            sum += polygon[index].Cross(polygon[(index + 1) % polygon.Count]);
        }

        return sum;
    }

    /// <summary>Carré de la distance de l'origine à un polygone convexe d'aire non nulle.</summary>
    private static Surd DistanceSquaredToOrigin(IReadOnlyList<Vec> polygon)
    {
        int orientation = TwiceArea(polygon).Sign;
        bool inside = true;
        Surd best = polygon[0].Dot(polygon[0]);
        for (int index = 0; index < polygon.Count; index++)
        {
            Vec start = polygon[index];
            Vec end = polygon[(index + 1) % polygon.Count];
            // L'origine est du côté intérieur de l'arête si edge × (O − start) a le signe de l'orientation.
            if ((start.Cross(end - start) * orientation).Sign < 0)
            {
                inside = false;
            }

            best = Surd.Min(best, DistanceSquaredToSegment(start, end));
        }

        return inside ? Surd.Zero : best;
    }

    private static Surd DistanceSquaredToSegment(Vec start, Vec end)
    {
        Vec edge = end - start;
        Surd lengthSquared = edge.Dot(edge);
        if (lengthSquared.Sign == 0)
        {
            return start.Dot(start);
        }

        Surd t = -start.Dot(edge) / lengthSquared;
        if (t.Sign <= 0)
        {
            return start.Dot(start);
        }

        if (t.CompareTo(1) >= 0)
        {
            return end.Dot(end);
        }

        Vec closest = start + edge * t;
        return closest.Dot(closest);
    }
}
