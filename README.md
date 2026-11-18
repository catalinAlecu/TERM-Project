# TERM

A starting point for a mobile application built with Python and [Flet](https://flet.dev/).

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python main.py
```

Flet opens the application in a desktop window by default. To run it in a browser:

```bash
flet run --web main.py
```

## Build for mobile

After installing the platform prerequisites required by Flet, build an Android package with:

```bash
flet build apk
```

The application entry point is `main.py`.
