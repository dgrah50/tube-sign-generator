import os
import pathlib

# Base directories
BASE_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()
FONTS_DIR = os.path.join(BASE_DIR, "app", "static", "fonts")
TEMPLATES_DIR = os.path.join(BASE_DIR, "app", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "app", "static")

# Ensure directories exist
for directory in [TEMPLATES_DIR, STATIC_DIR, FONTS_DIR]:
    os.makedirs(directory, exist_ok=True)

# Base image configuration
BASE_IMAGE_PATH = os.path.join(BASE_DIR, "app", "static", "images", "tube_sign2.png")

# Font configuration
DEFAULT_FONT = "reenie_beanie"

# Image generation settings
TEXT_POSITIONS = [
    {"y_offset": 35, "size": 38, "rotation": 2, "x": 170},
    {"y_offset": 90, "size": 34, "rotation": 1, "x": 172},
    {"y_offset": 115, "size": 33, "rotation": 3, "x": 168},
    {"y_offset": 185, "size": 35, "rotation": 0, "x": 171},
    {"y_offset": 210, "size": 32, "rotation": 2, "x": 169},
    {"y_offset": 255, "size": 34, "rotation": 1, "x": 173},
    {"y_offset": 272, "size": 33, "rotation": 3, "x": 170},
    {"y_offset": 315, "size": 32, "rotation": 2, "x": 169},
    {"y_offset": 355, "size": 34, "rotation": 1, "x": 173},
]

# Date and time text settings
DATE_TEXT_SETTINGS = {"size": 40, "rotation": 4, "x": 244, "y": 155}
TIME_TEXT_SETTINGS = {"size": 30, "rotation": 3, "x": 244, "y": 205}

# Base y-position for lines of text
BASE_Y_POSITION = 220
