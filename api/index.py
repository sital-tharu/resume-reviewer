from app import create_app

try:
    app = create_app()
    app.handler = app  # Required for Vercel
except Exception as e:
    import sys
    sys.stderr.write("APP ERROR: " + str(e) + "\n")
    raise
