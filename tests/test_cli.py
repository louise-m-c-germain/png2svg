from PIL import Image

from png2svg.cli import build_parser, main

def test_parser_input_and_output():
    args = build_parser().parse_args(["in.png", "out.svg"])
    assert args.input == "in.png"
    assert args.output == "out.svg"


def test_parser_default_radius():
    args = build_parser().parse_args(["in.png", "out.svg"])
    assert args.radius == 15


def test_parser_custom_radius():
    args = build_parser().parse_args(["in.png", "out.svg", "--radius", "25"])
    assert args.radius == 25


def test_main_writes_an_svg_file(monkeypatch, tmp_path):
    source = tmp_path / "in.png"
    Image.new("RGB", (60, 40), (255, 0, 0)).save(source)
    target = tmp_path / "out.svg"
    monkeypatch.setattr("sys.argv", ["png2svg", str(source), str(target)])
    main()
    assert target.read_text().startswith("<svg")