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
        a = i * math.pi / 3 + math.pi / 6
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        L.append((x, y))
    return L


def hexagonal_grid(width: int, height: int, r: float) -> list[tuple[float, float]]:
    """Return the centers of the hexagons covering an image of certain width and certain height.
    Args:
        width (int): width of the image in pixels.
        height (int): height of the image in pixels.
        r (float): radius of each hexagon.
    Returns:
        list of tuple: contains the coordinates of each hexagon center."""

    dx = math.sqrt(3) * r
    dy = 1.5 * r
    row = 0
    y = 0.0
    centers = []
    while y < height:
        x = 0.0 if row % 2 == 0 else dx / 2
        while x < width:
            centers.append((x, y))
            x = x + dx
        y = y + dy
        row = row + 1
    return centers
