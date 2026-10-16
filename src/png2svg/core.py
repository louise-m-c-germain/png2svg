"""Core geometry"""

import math

from PIL import Image


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


def average_color(image: Image.Image, cx: float, cy: float, r: float) -> tuple[int, int, int]:
    """Return the average RGB color sampled around(cx,cy).
    Args:
        image (Image.Image): the source image.
        cx (float): first coordinate of the hexagon center.
        cy (float): second coordinate of the hexagon center.
        r (float): radius of the hexagon.
    Returns:
        tuple of int: the average (red, green, blue) components."""
    red, green, blue = 0, 0, 0
    count = 0
    rgb = image.convert("RGB")
    for x in range(int(cx - r / 2), int(cx + r / 2 + 1)):
        for y in range(int(cy - r / 2), int(cy + r / 2 + 1)):
            if x < 0 or y < 0 or x >= rgb.width or y >= rgb.height:
                continue
            else:
                pr, pg, pb = rgb.getpixel((x, y))  # type: ignore[misc]
                red += pr
                green += pg
                blue += pb
                count += 1
    return (red // count, green // count, blue // count)
