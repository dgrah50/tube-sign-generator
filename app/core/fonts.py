import os
import glob
from app.config.settings import FONTS_DIR, DEFAULT_FONT


class FontManager:
    """
    Manages font discovery, loading, and selection.
    """

    def __init__(self):
        self.fonts = {}
        self.display_names = {}
        self._load_default_fonts()
        self._discover_fonts()

    def _load_default_fonts(self):
        """Load the default fonts that are guaranteed to exist."""
        self.fonts = {
            "reenie_beanie": os.path.join(FONTS_DIR, "Reenie_Beanie/ReenieBeanie.ttf"),
        }

    def _discover_fonts(self):
        """Discover additional fonts from the fonts directory."""
        font_files = glob.glob(os.path.join(FONTS_DIR, "**/*.ttf"), recursive=True)
        for font_file in font_files:
            font_name = os.path.basename(font_file).lower().replace(".ttf", "")
            if font_name not in self.fonts:
                self.fonts[font_name] = font_file

        # Create display names for all fonts
        self.display_names = {
            key: key.replace("_", " ").title() for key in self.fonts.keys()
        }

    def get_font_path(self, font_name=None):
        """
        Get the path to the specified font or default font if not found.

        Args:
            font_name: Name of the font to retrieve

        Returns:
            Path to the font file
        """
        if not font_name or font_name not in self.fonts:
            font_name = DEFAULT_FONT

        return self.fonts[font_name]

    def get_font_options_html(self):
        """
        Generate HTML options for a font selector dropdown.

        Returns:
            HTML string with options for the font dropdown
        """
        options = []
        for font_key, display_name in self.display_names.items():
            options.append(f'<option value="{font_key}">{display_name}</option>')
        return "\n".join(options)

    def get_available_fonts(self):
        """
        Get a dictionary of available fonts and their display names.

        Returns:
            Dictionary with font keys and display names
        """
        return self.display_names
