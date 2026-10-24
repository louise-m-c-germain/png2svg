import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import io

    import marimo as mo
    from PIL import Image

    from png2svg.core import build_svg

    return Image, build_svg, io, mo


@app.cell
def _(mo):
    file_picker = mo.ui.file(filetypes=[".png", ".jpg", ".jpeg"], label="Picture")
    radius = mo.ui.slider(5, 40, value=15, label="Hexagon radius")
    mo.hstack([file_picker, radius])
    return file_picker, radius


@app.cell
def _(Image, build_svg, file_picker, io, mo, radius):
    if not file_picker.value:
        output = mo.md("Chose an image.")
    else:
        image = Image.open(io.BytesIO(file_picker.value[0].contents))
        svg = build_svg(image, radius.value)
        output = mo.Html(svg)
    output
    return


if __name__ == "__main__":
    app.run()
