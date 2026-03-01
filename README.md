# Tube Sign Generator

Create London Underground-inspired service update signs from the browser.

This project is a Flask + Pillow web app that takes custom text, date/time values, and handwriting-style font choices, then renders a downloadable PNG sign in memory (no generated files are persisted on the server).

![Tube sign example](app/static/images/tube_sign2.png)

## Features

- Generate a custom tube-style sign image from form input
- Support up to 9 text lines plus optional date and time
- Live preview while editing
- Multiple bundled handwriting-style fonts
- Full-size PNG download
- Stateless image generation (in-memory response)

## Tech Stack

- Python 3.12
- Flask 3
- Pillow
- Gunicorn (production)

## Quick Start

1. Clone:
   ```bash
   git clone https://github.com/dgrah50/tube-sign-generator.git
   cd tube-sign-generator
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run locally:
   ```bash
   python run.py
   ```
5. Open:
   `http://localhost:5000`

## Usage

1. Open the homepage.
2. Enter text across the available lines.
3. Optionally set date and time.
4. Select a font.
5. Preview updates automatically.
6. Download the generated image.

## API Endpoints

- `GET /` - Main form UI
- `GET /preview` - Render preview PNG from query parameters
- `GET /image.png` - Render downloadable full-size PNG from query parameters

## Project Layout

```text
tube-sign-generator/
├── app/
│   ├── core/                 # Font loading + image generation logic
│   ├── routes/               # Flask routes and request handling
│   ├── static/               # Fonts + base sign image
│   └── templates/            # HTML templates
├── run.py                    # Local/dev entrypoint
├── main.py                   # Compatibility entrypoint
├── Procfile                  # Gunicorn process type (Heroku-style)
├── app.json                  # Heroku app metadata
├── requirements.txt
└── pyproject.toml
```

## Deployment

This repo includes `Procfile`, `runtime.txt`, and `app.json`, so it can be deployed on Heroku-style Python platforms directly.

Example process command:

```bash
gunicorn "app:create_app()"
```

## Development Notes

- Fonts are loaded from `app/static/fonts/`.
- Add a new `.ttf` file under that directory and restart the app to make it available.
- The root-level `app.py` is legacy; the package app (`app/`) is the active implementation.

## License

No license file is currently included in this repository. Add one (for example, MIT) before distributing or accepting external contributions.
