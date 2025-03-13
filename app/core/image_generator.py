from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from app.config.settings import (
    BASE_IMAGE_PATH,
    TEXT_POSITIONS,
    DATE_TEXT_SETTINGS,
    TIME_TEXT_SETTINGS,
    BASE_Y_POSITION,
)


class SignImageGenerator:
    """
    Handles the generation of tube sign images with text overlays.
    """

    def __init__(self, font_manager):
        """
        Initialize the image generator with font manager.

        Args:
            font_manager: FontManager instance to handle font selection
        """
        self.font_manager = font_manager

    def add_text(self, img, text, size, rotation, x, y, font_path):
        """
        Draw rotated text onto the base image using a separate overlay.

        Args:
            img: PIL Image object to draw on
            text: Text to draw
            size: Font size
            rotation: Text rotation in degrees
            x, y: Position coordinates
            font_path: Path to the font file
        """
        font = ImageFont.truetype(font_path, size)
        # Make an RGBA image for the text so we can rotate it cleanly
        txt_img = Image.new("RGBA", (600, 200), (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_img)
        draw.text((0, 0), text, font=font, fill=(0, 0, 0))
        txt_img = txt_img.rotate(rotation, expand=True)
        # Alpha composite so the rotated text merges nicely
        img.alpha_composite(txt_img, (x, y))

    def generate_image(self, date_str="", time_str="", text_lines=None, font_name=None):
        """
        Generate a tube sign image with the provided text in memory.

        Args:
            date_str: Date string to display
            time_str: Time string to display
            text_lines: List of lines to display (max 9)
            font_name: Name of the font to use

        Returns:
            BytesIO object containing the image data
        """
        if text_lines is None:
            text_lines = []

        # Get font path
        font_path = self.font_manager.get_font_path(font_name)

        # Open and prepare the base image
        base_img = Image.open(BASE_IMAGE_PATH).convert("RGBA")

        # Add date if provided
        if date_str:
            self.add_text(
                base_img,
                date_str,
                size=DATE_TEXT_SETTINGS["size"],
                rotation=DATE_TEXT_SETTINGS["rotation"],
                x=DATE_TEXT_SETTINGS["x"],
                y=DATE_TEXT_SETTINGS["y"],
                font_path=font_path,
            )

        # Add time if provided
        if time_str:
            self.add_text(
                base_img,
                time_str,
                size=TIME_TEXT_SETTINGS["size"],
                rotation=TIME_TEXT_SETTINGS["rotation"],
                x=TIME_TEXT_SETTINGS["x"],
                y=TIME_TEXT_SETTINGS["y"],
                font_path=font_path,
            )

        # Add text lines
        for i, line in enumerate(text_lines[:9]):  # Limit to 9 lines
            if not line:
                continue

            position = TEXT_POSITIONS[i]
            self.add_text(
                base_img,
                line,
                size=position["size"],
                rotation=position["rotation"],
                x=position["x"],
                y=BASE_Y_POSITION + position["y_offset"],
                font_path=font_path,
            )

        # Save the image to a BytesIO object instead of a file
        img_io = BytesIO()
        base_img.save(img_io, "PNG")
        img_io.seek(0)  # Move to the beginning of the BytesIO buffer

        return img_io
