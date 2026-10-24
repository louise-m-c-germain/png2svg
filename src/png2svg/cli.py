"""Command-line interface for png2svg."""

import argparse

from PIL import Image

from png2svg.core import build_svg, write_svg


def build_parser() -> argparse.ArgumentParser:
    """Return the argument parser of the png2svg command."""
    parser = argparse.ArgumentParser(
        prog="png2svg", description="Convert a picture into a scalable hexagonal SVG."
    )
    parser.add_argument("input", help="Path of the picture to convert.")
    parser.add_argument("output", help="Path of the SVG file to create.")
    parser.add_argument(
        "--radius",
        type=float,
        default=15,
        help="Radius of each hexagon in pixels (default: 15).",
    )
    return parser


def main() -> None:
    """Convert the input picture into an SVG file."""
    args = build_parser().parse_args()
    image = Image.open(args.input)
    write_svg(build_svg(image, args.radius), args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
