from png2svg.core import hexagon_vertices


def test_hexagon_vertices():
    vertices = hexagon_vertices(0, 0, 5)
    assert vertices[0] == (5, 0)


def test_len_hexagon_vertices():
    n = len(hexagon_vertices(1, 3, 7))
    assert n == 6
