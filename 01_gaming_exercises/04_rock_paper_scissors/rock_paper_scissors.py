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
welcome {player_name} the Rock, Paper, Scissors Robot
Its Time To Play ROCK, PAPER, SCISSORS.
      
You have probably played lost in this MANY TIME and know the rules but for those who dont know
You will pick from ROCK, PAPER, OR SCISSORS.
The CPU will select ROCK, PAPER, OR SCISSORS at Random
      
1) ROCK OBLITERATES SCISSORS
2) SCISSORS SLICES PAPER
3) PAPER KIDNAPS ROCK
""")

# MULI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of duoble-quotes is just ignored.
If you you need to write large comments, it's easier to use multi-line strings than
putting a # in front
"""

# MAIN GAME LOOP
while player_score < 5 and cpu_score < 5:
    print(f"{player_name} you have {player_score} points. \nThe CPU has {cpu_score} points\n")
    player_choice = input("Please enter rock, paper or scissors and press enter\n").lower()
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Please enter rock, paper or scissors and press enter\n").lower()
        if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
            print("You are not folleing directions.  Please try again.\n")
            exit()
        print(f"you have chosen {player_choice}.\n")
    else:
        print(f"you have chosen {player_choice}.\n")

    # print the current score for CPU and Player
    # let player select rock, paper, scissors
    cpu_choice = random.randint(0,2) # randomly select 0, 1 or 2.
    if cpu_choice == 0:
        cpu_choice = "rock"
    elif cpu_choice == 1:
        cpu_choice = "scissors"
    elif cpu_choice == 2:
        cpu_choice = "paper"
    else:
        print("Some how you broke the cpu's choice:/. \n please restart program if you can even do that")
        exit()
    print(f"CPU Choice: {cpu_choice}")

    # let CPU select choice at random
    # Compare player vhoice to cpu choice
    # print results to the screen
    # award poiny to winner and output results