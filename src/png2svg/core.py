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


def hexagon_polygon(vertices: list[tuple[float, float]], color: tuple[int, int, int]) -> str:
    """Return the SVG polygon element for one hexagon.
    Args :
        vertices (list of tuples): list of the coordinates of vertices.
        color (tuple of int): the (red, green, blue) fill color.
    Returns :
        str: the SVG polygon element as a string."""
    points = " ".join(f"{x},{y}" for x, y in vertices)
    red, green, blue = color
    return f'<polygon points="{points}" fill="rgb({red},{green},{blue})"/>'


def build_svg(image: Image.Image, r: float) -> str:
    """Return the full SVG document rendering an image as hexagons.
    Args:
        image (Image.Image): the source image.
        r (float): radius of each hexagon.
    Returns:
        str: the complete SVG document."""
    polygons = []
    centers = hexagonal_grid(image.width, image.height, r)
    for cx, cy in centers:
        vertices = hexagon_vertices(cx, cy, r)
        color = average_color(image, cx, cy, r)
        polygons.append(hexagon_polygon(vertices, color))
    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{image.width}" height="{image.height}">'
    )
    body = "\n".join(polygons)
    return f"{header}\n{body}\n</svg>"


def write_svg(svg: str, output_path: str) -> None:
    """Write an SVG document to a file.
    Args:
        svg (str): the SVG document.
        output_path (str): path of the file to create.
    Returns:
        None"""
    with open(output_path, "w") as f:
        f.write(svg)
