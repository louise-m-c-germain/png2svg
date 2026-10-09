"""Core geometry"""

import math


def hexagon_vertices(cx: float, cy: float, r: float) -> list[tuple[float, float]]:
    """Return the 6 vertices of an hexagon centered on (cx,cy).
    Args:
        cx (float): first coordinate of the center.
        cy (float): second coordinate of the center.
        r (float): radius
    Returns:
        list of tuple: contains the 6 tuple of vertices' coordinates."""
    L = []
    for i in range(6):
        a = i * math.pi / 3
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        L.append((x, y))
    return L
