# index.py
print("API INDEX.PY STARTED")

try:
    from app import create_app
    app = create_app()
    app.handler = app  # Required by Vercel
except Exception as e:
    import sys
    sys.stderr.write("APP ERROR: " + str(e) + "\n")
    raise
