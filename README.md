# png2svg

Convert a raster picture into a scalable SVG made of hexagons. The output can be
enlarged without any loss of quality, for instance as a high-resolution wallpaper.

![A photograph and its SVG conversion](example-photo.png)
*A photograph (left) and its SVG conversion with `--radius 5` (right).*

![The reference picture and its SVG conversion](example-reference.png)
*The reference picture from the assignment (left) and its conversion with `--radius 15` (right).*

## How it works

A hexagonal grid is laid over the input picture. For each hexagon, the average
colour of the pixels sampled around its centre is computed, and the hexagon is
written to the SVG document with that colour. A background rectangle fills the
gaps left by the hexagons cut off at the edges.

The grid uses point-up hexagons: neighbouring centres are `√3 × r` apart
horizontally and `1.5 × r` apart vertically, with every other row shifted by half 
a step.

## Installation

```bash
git clone https://github.com/louise-m-c-germain/png2svg.git
cd png2svg
uv sync
```

## Command-line usage

```bash
uv run png2svg picture.png output.svg
uv run png2svg picture.png output.svg --radius 25
```

| Argument | Meaning | Default |
| --- | --- | --- |
| `input` | picture to convert (PNG, JPEG, any format Pillow can read) | required |
| `output` | SVG file to create | required |
| `--radius` | radius of each hexagon, in pixels | 15 |

A smaller radius keeps more detail; a larger one gives a coarser mosaic.

Run `uv run png2svg --help` for the full help message.

## Interactive notebook

```bash
uv run marimo edit notebooks/png2svg_explorer.py
```

The notebook lets you pick a picture, set the radius with a slider, and see the
converted result update live.

## Library usage

```python
from PIL import Image

from png2svg.core import build_svg, write_svg

image = Image.open("picture.png")
write_svg(build_svg(image, 15), "output.svg")
```

The library exposes six functions:

| Function | Purpose |
| --- | --- |
| `hexagon_vertices(cx, cy, r)` | the six vertices of one hexagon |
| `hexagonal_grid(width, height, r)` | the centres covering a picture |
| `average_color(image, cx, cy, r)` | the average colour around a centre |
| `hexagon_polygon(vertices, color)` | one SVG `<polygon>` element |
| `build_svg(image, r)` | the complete SVG document |
| `write_svg(svg, path)` | write the document to a file |

## Development

```bash
uv run ruff format .                                # formatting
uv run ruff check .                                 # linting
uv run mypy src                                     # type checking
uv run pytest --cov=src --cov-report=term-missing   # tests and coverage
```

Every push to `main` replays these four checks on Python 3.11, 3.12 and 3.13
through GitHub Actions. Test coverage must stay above 90%.

The project was developed test-first: each feature was declared as a GitHub
issue, implemented on its own branch following the red-green-refactor cycle, and
merged into `main` once the tests passed.

## Project layout

```text
png2svg/
├── .github/workflows/
│   └── tests.yml              # formatting, linting, typing, tests
├── notebooks/
│   └── png2svg_explorer.py    # interactive marimo notebook
├── src/png2svg/
│   ├── __init__.py
│   ├── core.py                # conversion library
│   └── cli.py                 # command-line interface
├── tests/
│   ├── test_core.py
│   └── test_cli.py
├── pyproject.toml
├── uv.lock
└── README.md
```