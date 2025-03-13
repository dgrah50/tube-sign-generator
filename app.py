#!/usr/bin/env python3
from flask import Flask, request, send_file, make_response, render_template

from fonts import FontManager
from image_generator import SignImageGenerator

# Initialize Flask application
app = Flask(__name__, template_folder="templates")

# Initialize font manager and image generator
font_manager = FontManager()
image_generator = SignImageGenerator(font_manager)


@app.route("/")
def index():
    """
    Render the main index page with the sign creation form.
    """
    font_options = font_manager.get_font_options_html()
    return render_template("index.html", font_options=font_options)


@app.route("/image.png")
def generate_image():
    """
    Creates a London Underground-style sign image with
    optional date/time and up to 9 lines of text.
    """
    # Extract request parameters
    date_str = request.args.get("date", "").strip()
    time_str = request.args.get("time", "").strip()
    selected_font = request.args.get("font", "").strip()

    # Extract text lines
    text_lines = []
    for key in [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
    ]:
        val = request.args.get(f"text[{key}]", "").strip()
        if val:
            text_lines.append(val)

    # Generate the image in memory
    img_io = image_generator.generate_image(
        date_str=date_str,
        time_str=time_str,
        text_lines=text_lines,
        font_name=selected_font,
    )

    # Send the image directly from memory
    return send_file(img_io, mimetype="image/png")


@app.route("/preview")
def preview_image():
    """
    Creates a preview image for live updates in the UI.
    Uses the same logic as generate_image.
    """
    # Extract request parameters
    date_str = request.args.get("date", "").strip()
    time_str = request.args.get("time", "").strip()
    selected_font = request.args.get("font", "").strip()

    # Extract text lines
    text_lines = []
    for key in [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
    ]:
        val = request.args.get(f"text[{key}]", "").strip()
        if val:
            text_lines.append(val)

    # Generate the image in memory
    img_io = image_generator.generate_image(
        date_str=date_str,
        time_str=time_str,
        text_lines=text_lines,
        font_name=selected_font,
    )

    # Send the image directly from memory
    return send_file(img_io, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
