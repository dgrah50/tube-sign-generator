#!/usr/bin/env python3
"""
Main entry point for the Tube Sign Generator application.
"""

import os
from app import create_app

if __name__ == "__main__":
    app = create_app()
    # Get port from environment variable or use default (5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
