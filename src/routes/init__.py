from .game import game_blueprint

def init_routes(app):
    """
    Function to initialize and register routes (Blueprints) with the Flask app.
    """
    app.register_blueprint(game_blueprint, url_prefix='/api/game')  # Register the game Blueprint
