# Rock, paper, Scissiors bt Calvin Young, v0.7.5

# MODULE IMPORTS
import random

#DATA STRUCTURES -- PLAYER
player_name = "test_player"
player_score = 0
player_choice = None

 #DATA STRUCTURES -- CPU
cpu_score = 0
cpu_choice = None

# PLAYER NAME INPUT
player_name = input("Please type yourn name here and press enter.\n")
print(f"Hello {player_name}!\n")
isCorrect = input ("Is that correct? Type yes or no and press enter.\n").lower()



if isCorrect == "yes":
    print(f"ok {player_choice}, let's play Rock, Paper, Scissors!\n")
else:
    player_name = input("please type your name and press enter.\n")