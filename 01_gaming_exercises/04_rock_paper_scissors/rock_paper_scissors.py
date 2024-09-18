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

# .lower() can turn ALL input into lowercase
# .upper() can turn ALL input into UPPERCASE

if isCorrect == "yes":
    print(f"ok {player_choice}, let's play Rock, Paper, Scissors!\n")
else:
    player_name = input("please type your name and press enter.\n")

# THE RULES
print("""
welcome to the Rock, Paper, Scissors Robot
Its Time To Play ROCK, PAPER, SCISSORS.
      
You have probably played lost in this MANY TIME and know the rules but for those who dont know
You will pick from ROCK, PAPER, OR SCISSORS.
The CPU will select ROCK, PAPER, OR SCISSORS at Random
      
1) ROCK OBLITERATES SCISSORS
2) SCISSORS SLICES PAPER
3) PAPER DESTROYS ROCK
""")

# MULI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of duoble-quotes is just ignored.
If you you need to write large comments, it's easier to use multi-line strings than
putting a # in front
"""

# MAIN GAME LOOP
while player_name < 5 and cpu_score < 5:
    print(f"{player_name} you have {player_score} points. \nThe CPU has {cpu_score} points\n")
    player_choice = input("Please enter rock, paper or scissors and press enter\n").lower()
    if player_choice != "rock" or player_choice != "paper" or player_choice != "scissors":
        player_choice = input("Please enter rock, paper or scissors and press enter\n").lower()
        if player_choice != "rock" or player_choice != "paper" or player_choice != "scissors":
            print("You are not folleing directions.  Please try again.\n")
            exit()
            print(f"you have chosen {player_choice}.\n")
    else:
        print(f"you have chosen {player_choice}.\n")

    # print the current score for CPU and Player
    # let player select rock, paper, scissors
    # let CPU select choice at random
    # Compare player vhoice to cpu choice
    # print results to the screen
    # award poiny to winner and output results