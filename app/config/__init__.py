"""
Application configuration module.
"""

import os


# Define environment-specific configurations
class Config:
    """Base configuration class."""

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    """Production-specific configuration."""

    pass


class DevelopmentConfig(Config):
    """Development-specific configuration."""

    DEBUG = True


class TestingConfig(Config):
    """Testing-specific configuration."""

    TESTING = True
    DEBUG = True


# Map environment names to configuration classes
config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}


# Function to get current configuration based on environment
def get_config():
    """Get the configuration based on the environment."""
    env = os.getenv("FLASK_ENV", "default")
    return config_by_name[env]
