import math

from PIL import Image

from png2svg.core import average_color, hexagon_vertices, hexagonal_grid

# Tests gro hexagon_vertices


def test_vertices_radiu():
    cx, cy, r = 0, 0, 5
    for x, y in hexagon_vertices(cx, cy, r):
        assert math.isclose(math.dist((cx, cy), (x, y)), r)


def test_len_hexagon_vertices():
    n = len(hexagon_vertices(1, 3, 7))
    assert n == 6


# Tests for hexagonal_grid


def test_first_center_hexagonal_grid():
    centers = hexagonal_grid(100, 100, 10)
    assert centers[0] == (0, 0)


def test_centers_cover_the_image():
    width, height, r = 100, 80, 10
    centers = hexagonal_grid(width, height, r)
    for x, y in centers:
        assert 0 <= x < width
        assert 0 <= y < height


# Tests for average_color


def test_uniform_image():
    image = Image.new("RGB", (100, 100), (255, 0, 0))
    assert average_color(image, 50, 50, 10) == (255, 0, 0)


def test_average_two_colors():
    image = Image.new("RGB", (100, 100), (0, 0, 0))
    for x in range(50):
        for y in range(100):
            image.putpixel((x, y), (255, 255, 255))
    red, green, blue = average_color(image, 50, 50, 20)
    assert 0 < red < 255
    assert red == green == blue
