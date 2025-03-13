# Tube Sign Generator

A web application that creates custom London Underground-style service information signs. 
Users can add text, customize dates/times, and select different fonts to create unique signs.

## Features

- Create custom tube-style service information signs
- Add date and time information 
- Up to 9 lines of customizable text
- Multiple font options
- Live preview as you type
- Download generated images at full resolution
- Memory-efficient: no images are stored on the server

## Project Structure

The application follows a standard Python package structure:

```
tube-sign-generator/
├── app/                      # Main application package
│   ├── __init__.py           # Application factory
│   ├── config/               # Configuration module
│   │   ├── __init__.py
│   │   └── settings.py       # Configuration settings
│   ├── core/                 # Core business logic
│   │   ├── __init__.py
│   │   ├── fonts.py          # Font management
│   │   └── image_generator.py# Image generation
│   ├── routes/               # Web routes
│   │   ├── __init__.py
│   │   └── views.py          # Route handlers
│   ├── static/               # Static assets
│   │   ├── fonts/            # Font files
│   │   └── images/           # Images including tube_sign2.png
│   └── templates/            # HTML templates
│       └── index.html        # Main UI template
├── run.py                    # Main entry point
├── main.py                   # Backward compatibility entry point
├── Procfile                  # Heroku deployment configuration
├── runtime.txt               # Python version for Heroku
├── app.json                  # Heroku application metadata
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/tube-sign-generator.git
   cd tube-sign-generator
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application Locally

Start the Flask development server:

```
python run.py
```

Or if you prefer to use the original script:

```
python main.py
```

Access the application in your web browser at: http://localhost:5000

## Deploying to Heroku

### Option 1: Deploy with Heroku CLI

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if you haven't already
2. Log in to Heroku:
   ```
   heroku login
   ```
3. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```
4. Push your code to Heroku:
   ```
   git push heroku main
   ```
5. Open your app in a browser:
   ```
   heroku open
   ```

### Option 2: Deploy with Heroku Dashboard

1. Create a new app from the [Heroku Dashboard](https://dashboard.heroku.com/apps)
2. Connect your GitHub repository or use Heroku Git
3. Enable automatic deploys or manually deploy
4. Open your app from the Heroku Dashboard

### Option 3: Deploy with the Deploy to Heroku Button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Usage

1. Fill in the form fields with your desired text
2. Select a font from the dropdown menu
3. Enter a date and/or time if desired
4. The preview updates automatically as you type
5. Click "Download Full Size Image" to get the final PNG file

## Development

### Adding New Fonts

To add new fonts:

1. Create a new directory in the `app/static/fonts/` folder for your font family
2. Add the TTF font file(s) to this directory
3. Restart the application - fonts are discovered automatically

## Technical Details

All images are generated on-demand in memory and served directly to the user. No images are stored on the server, making this application efficient and suitable for environments with limited disk space.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Inspired by London Underground service information signs
- Uses Flask for the web framework and Pillow for image processing
