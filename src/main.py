from flask import Flask
from .routes.game import game_blueprint
from .config import Config
def init_routes(app):
    """
    Function to initialize and register routes (Blueprints) with the Flask app.
    """
    app.register_blueprint(game_blueprint, url_prefix='/api/game') 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
