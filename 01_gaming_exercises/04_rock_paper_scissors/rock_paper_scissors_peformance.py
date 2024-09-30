# Rock, paper, Scissiors bt Calvin Young, v0.7.5

# MODULE IMPORTS
import random, time

#DATA STRUCTURES -- PLAYER
num_draws = 0
player_score = 0
player_choice = None

 #DATA STRUCTURES -- CPU
cpu_score = 0
cpu_choice = None

# MAIN GAME LOOP
loop_count = 0
loops_req = int(input("How many loops do you want?\nEnter an interger, no commas, and pruss enter.\n"))
# req in the universal abbreviation in computer programing for request. req = request
rps_time_start = time.time() # returns the number of seconds since jan. 01, 1970 @ 12:00AM
while loop_count < loops_req:

    # let player select rock, paper, scissors
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
    print(f"CPU Choice: {cpu_choice}")

  # let PLAYER select choice at random
    player_choice = random.randint(0,2) # randomly select 0, 1 or 2.
    if  player_choice == 0:
         player_choice = "rock"
    elif  player_choice == 1:
         player_choice = "paper"
    elif  player_choice == 2:
         player_choice = "scissors"
    else:
        print("Some how you broke the cpu's choice:/. \n please restart program if you can even do that\n")
        exit()

    if player_choice == "rock"and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("The CPU won a point get better\n")
        cpu_score += 1
        # CPU wins
    elif player_choice == "rock"and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("you won a point\n")
        player_score += 1
        # PLAYER wins
    elif player_choice == "rock"and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("You both chose the same answer its a draw\n")
        # Draw
    elif player_choice == "scissors"and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("you won a point\n")
        player_score += 1
        # PLAYER wins
    elif player_choice == "scissors"and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("You both chose the same answer its a draw\n")
        # Draw
    elif player_choice == "scissors"and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("The CPU won a point get better\n")
        cpu_score += 1
        # CPU wins
    elif player_choice == "paper"and cpu_choice == "paper":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("You both chose the same answer its a draw\n")
        # Draw
    elif player_choice == "paper"and cpu_choice == "scissors":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("The CPU won a point get better\n")
        cpu_score += 1
        # CPU wins
    elif player_choice == "paper"and cpu_choice == "rock":
        print(f"The CPU chose {cpu_choice} and you chose {player_choice}\n")
        print("you won a point\n")
        player_score += 1
        # PLAYER wins
    else:
        print("Sorry cant find the winner. Looks like you gotta restart.\n")
        exit()
    loop_count += 1


print(f"Your Final Score: {player_score}CPU Final Score{cpu_score}\n")
if player_score > cpu_score:
    print(f"Nice jod you won against an A.I. in the most simple game in the world when you could have been doing something with your life.\n")
elif cpu_score > player_score:
    print(f"Just amazing you lost in ROCK, PAPER, SCISSORS, the most simple game in the world you just suck a life.\n")
else:
    print("Sorry cant find the winner. Looks like you gotta restart.\n")
    exit()

    rps_time_stop = time.time ()
    rps_time = rps_time_stop - rps_time_start
    print(f"Number of loops: {loop_count}\n")
    print(f"Exucution Time {rps_time: .2f}")


num



    # let CPU select choice at random
    # Compare player vhoice to cpu choice
    # print results to the screen
    # award poiny to winner and output results