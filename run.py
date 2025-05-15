# Entry point for the Flask application
# This file creates and runs the Flask app using the factory pattern

from app import create_app  # Import the app factory function

app = create_app()  # Create the Flask app instance

if __name__ == '__main__':
    # Run the Flask development server in debug mode
    app.run(debug=True)