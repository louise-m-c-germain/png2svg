import math

from PIL import Image

from png2svg.core import (
    average_color,
    build_svg,
    hexagon_polygon,
    hexagon_vertices,
    hexagonal_grid,
    write_svg,
)

# Tests for hexagon_vertices


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


# Tests for hexagon_polygon


def test_hexagon_polygon_return():
    assert (
        hexagon_polygon([(10, 0), (18.6, 5), (4, 5), (8, 9), (1, 2), (0, 6)], (255, 0, 0))
        == '<polygon points="10,0 18.6,5 4,5 8,9 1,2 0,6" fill="rgb(255,0,0)"/>'
    )


# Tests for build_svg


def test_build_svg_structure():
    image = Image.new("RGB", (100, 80), (255, 0, 0))
    svg = build_svg(image, 10)
    assert svg.startswith("<svg")
    assert svg.endswith("</svg>")
    assert "<polygon" in svg


def test_build_background():
    image = Image.new("RGB", (100, 80), (255, 0, 0))
    assert "<rect" in build_svg(image, 10)


# Tests for write_svg


def test_write_svg_creates_a_file(tmp_path):
    output = tmp_path / "out.svg"
    write_svg("<svg></svg>", str(output))
    assert output.read_text() == "<svg></svg>"

