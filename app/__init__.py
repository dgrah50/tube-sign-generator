from flask import Flask
from app.config import get_config

# Initialize global objects
font_manager = None
image_generator = None


def create_app(config_class=None):
    """
    Create and configure the Flask application.

    Args:
        config_class: Optional configuration class to use

    Returns:
        Flask application instance
    """
    # Import here to avoid circular imports
    from app.core.fonts import FontManager
    from app.core.image_generator import SignImageGenerator
    from app.routes.views import views

    # Create Flask app
    app = Flask(__name__)

    # Configure the application
    if config_class is None:
        # Use environment-based configuration
        config_class = get_config()
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(views)

    # Initialize global instances
    global font_manager, image_generator
    font_manager = FontManager()
    image_generator = SignImageGenerator(font_manager)

    return app
