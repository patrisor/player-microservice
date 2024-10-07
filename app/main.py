from flask import Flask
from app.routes import register_routes

def create_app():
    """
    Function to create and configure a Flask application.
    
    Returns:
        Flask: A Flask application instance.
    """
    app = Flask(__name__)
    register_routes(app)  # Register all routes for the REST API
    return app

if __name__ == '__main__':
    # Create an application instance and run the development server.
    app = create_app()
    # Start Flask development server that listens on all network interfaces.
    app.run(host='0.0.0.0', port=5001, debug=True)