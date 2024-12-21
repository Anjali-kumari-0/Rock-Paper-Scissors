# from flask import Blueprint, request, jsonify
# from src.services.game_service import determine_winner

# game_blueprint = Blueprint('game', __name__)

# @game_blueprint.route('/play', methods=['POST'])
# def play():
#     data = request.json
#     player_choice = data.get('player_choice')
#     if player_choice not in ['rock', 'paper', 'scissors']:
#         return jsonify({"error": "Invalid choice"}), 400
    
#     result = determine_winner(player_choice)
#     return jsonify(result)


from flask import Blueprint, request, jsonify
from src.services.game_service import determine_winner
game_bleprint= Blueprint("game",__name__)
@game_bleprint.route("/play", methods=['POST'])
def play():
    data= request.json
    player_choice= data.get('player_choice')
    if player_choice not in  ['rock','paper','scissors']:
        return jsonify({"result":"invalid choice"})
    
    result= determine_winner(player_choice)
    return jsonify(result)
