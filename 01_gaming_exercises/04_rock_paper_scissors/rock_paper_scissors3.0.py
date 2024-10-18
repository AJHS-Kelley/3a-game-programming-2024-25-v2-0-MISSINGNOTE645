# Rock, paper, Scissiors bt Calvin Young, v3.0

# MODULE IMPORTS
import random

#DATA STRUCTURES -- PLAYER
player_name = "test player"
player_score = 0
player_choice = None

 #DATA STRUCTURES -- CPU
cpu_score = 0
cpu_choice = None

# PLAYER NAME INPUT
def player_name() -> str: # Function Signature -- name of function, (arguments if any)
    """Gets the name form the player and returns it."""
    # The line above is a DOCSTRING, it gives a brief example of what the function does.
    player_name = input("Please type your name here and press enter.\n")
    print(f"Hello {player_name}!\n")
    isCorrect = input ("Is that correct? Type yes or no and press enter.\n").lower()
    if isCorrect == "yes":
        print(f"ok {player_choice}, let's play Rock, Paper, Scissors!\n")
    else:
        player_name = input("please type your name and press enter.\n")
    return player_name

# CALLING THE FUNCTION
player_name = player_name() 

# THE RULES
def rules() -> None:
    """This function prints the rules of rock, paper, scissors."""
    print(f"""
    welcome {player_name} the Rock, Paper, Scissors Robot
    Its Time To Play ROCK, PAPER, SCISSORS.
        
    You have probably played lost in this MANY TIME and know the rules but for those who dont know
    You will pick from ROCK, PAPER, OR SCISSORS.
    The CPU will select ROCK, PAPER, OR SCISSORS at Random
        
    1) ROCK OBLITERATES SCISSORS
    2) SCISSORS SLICES PAPER
    3) PAPER KIDNAPS ROCK
    """)
    # Does anouther part of this program need to access this infomation?
    #IF YES, YOU MUST HAVE A return STATMENT
    #IF NO, A return STATMENT IS NOT REQUIRED

def player_choice() -> str:
    """This function allows player to chose rock, paper, scissors"""
    player_choice = input("Please enter rock, paper or scissors and press enter\n").lower()
    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Please enter rock, paper or scissors and press enter\n").lower()
        if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
            print("You are not folleing directions.  Please try again.\n")
            exit()
        print(f"you have chosen {player_choice}.\n")
    else:
        print(f"you have chosen {player_choice}.\n")
    return player_choice

def cpu_choice()-> str:
    """This function allows CPU to chose rock, paper, scissors"""
    cpu_choice = random.randint(0,2) # randomly select 0, 1 or 2.
    if cpu_choice == 0:
        cpu_choice = "rock"
    elif cpu_choice == 1:
        cpu_choice = "paper"
    elif cpu_choice == 2:
        cpu_choice = "scissors"
    else:
        print("Some how you broke the cpu's choice:/. \n please restart program if you can even do that\n")
        exit()
    return cpu_choice

def pick_winner(player_choice: str, cpu_choice: str) -> str: # playerchoice and cpuchoice and both ARGUMENTS, they will be string values.
    """This function uses the player choice and CPU choice to dertermine a winner."""
    if player_choice == "rock"and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("The CPU won a point get better\n")
        cpu_score += 1
        return "CPU wins"
            # CPU wins
    elif player_choice == "rock"and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("you won a point\n")
        player_score += 1
        return "Player wins"
            # PLAYER wins
    elif player_choice == "rock"and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("You both chose the same answer its a draw\n")
        return "Draw"
        # Draw
    elif player_choice == "scissors"and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("you won a point\n")
        player_score += 1
        return "Player wins"
            # PLAYER wins
    elif player_choice == "scissors"and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("You both chose the same answer its a draw\n")
        return "Draw"
            # Draw
    elif player_choice == "scissors"and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("The CPU won a point get better\n")
        cpu_score += 1
        return "CPU wins"
            # CPU wins
    elif player_choice == "paper"and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("You both chose the same answer its a draw\n")
        return "Draw"
            # Draw
    elif player_choice == "paper"and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("The CPU won a point get better\n")
        cpu_score += 1
        return "CPU wins"
            # CPU wins
    elif player_choice == "paper"and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("you won a point\n")
        player_score += 1
        return "Player wins"
            # PLAYER wins
    else:
        print("Sorry cant find the winner. Looks like you gotta restart.\n")
        exit()   
# MAIN GAME LOOP
while player_score < 5 and cpu_score < 5:
    print(f"{player_name} you have {player_score} points. \nThe CPU has {cpu_score} points\n")
   

    # let cpu select at random

   # print(f"CPU Choice: {cpu_choice}")

   # compaer player choice



print(f"Your Final Score: {player_score}CPU Final Score{cpu_score}\n")
if player_score > cpu_score:
    print(f"Nice jod {player_name} you won against an A.I. in the most simple game in the world when you could have been doing something with your life.\n")
elif cpu_score > player_score:
    print(f"Just amazing {player_name} you lost in ROCK, PAPER, SCISSORS, the most simple game in the world you just suck a life.\n")
else:
    print("Sorry cant find the winner. Looks like you gotta restart.\n")
    exit()







    # let CPU select choice at random
    # Compare player vhoice to cpu choice
    # print results to the screen
    # award poiny to winner and output results