from app import create_app

app = create_app()

# Required for Vercel
app.handler = app

try:
    from app import create_app
    app = create_app()
    app.handler = app
except Exception as e:
    import sys
    sys.stderr.write("APP ERROR: " + str(e) + "\n")
    raise
