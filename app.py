# from flask import Flask, request, render_template

# app= Flask(__name__) # __name__ is entery point of a program
#   # simplae flask app
  
# @app.route("/",methods=["GET"])
# def hello():
#     return 'hello world'

# @app.route("/2",methods=["GET"])
# def hello2():
#     return 'hello world 2'

# @app.route("/prams/<num>",methods=["GET"])
# def suc(num):
#     return 'hello world'+ num

# @app.route("/prams/<int:num>",methods=["GET"])
# def suc(num):
#     return 'hello world'+ str(num)

# @app.route("/form",methods=["GET","POST"]) #get hai ya post usko identify krne ke liye request class
# def form():
#     if request.method == "GET":
#         return render_template('form.html')

# if __name__=="__main__":
#     app.run(debug=True) # app.run port aur url leta philhal ke liye default localhost hoga
    
    
    
# from flask import Flask
# from src.routes.game import game_blueprint
# from src.config import Config
# def init_routes(app):
#     """
#     Function to initialize and register routes (Blueprints) with the Flask app.
#     """
#     app.register_blueprint(game_blueprint, url_prefix='/api/game') 

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     init_routes(app)
#     return app

# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)



from flask import Flask
from src.config import Config
from src.routes.game import game_blueprint
def init_route(app):
    app.register_blueprint(game_blueprint, url_prifix="api/game")
def create_ap():
    app= Flask(__name__)
    app.config.from_object(Config)
    init_route(app)
    return app

if __name__=="__main__":
    app= create_ap()
    app.run(debug=True)