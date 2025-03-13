#!/usr/bin/env python3
"""
Main entry point for the Tube Sign Generator application.
This file exists for backward compatibility with the original codebase.
The actual application logic is in app/__init__.py.
"""

import os

if __name__ == "__main__":
    # Import and run the Flask application
    from app import create_app

    app = create_app()
    # Get port from environment variable or use default (5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
