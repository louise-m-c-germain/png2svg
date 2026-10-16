import math

from png2svg.core import hexagon_vertices, hexagonal_grid

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
