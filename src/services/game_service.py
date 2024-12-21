# import random

# CHOICES = ['rock', 'paper', 'scissors']

# def determine_winner(player_choice):
#     computer_choice = random.choice(CHOICES)
#     if player_choice == computer_choice:
#         return {"result": "draw", "computer_choice": computer_choice}
    
#     rules = {
#         'rock': 'scissors',
#         'paper': 'rock',
#         'scissors': 'paper'
#     }

#     if rules[player_choice] == computer_choice:
#         return {"result": "win", "computer_choice": computer_choice}
#     else:
#         return {"result": "lose", "computer_choice": computer_choice}


import random
CHOICES=['rock','paper','scissors']
def determine_winner(player_choice):
    computer_choice= random.choice(CHOICES)
    if computer_choice == player_choice:
        result={"computer_choice":computer_choice,"result":"draw"}
        return result
    rules={
        'paper':'rock',
        'rock':'scissors',
        'scissors':'rock'
    }
    if rules[player_choice]== computer_choice:
        result={"computer_choice":computer_choice,"result":"win"}
        return result
    else:
        result={"computer_choice":computer_choice,"result":"lose"}
        return result
    
    
    
    