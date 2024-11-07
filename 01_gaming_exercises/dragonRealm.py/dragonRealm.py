# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

yourHealth = 0
yourChoice = None

dragonHealth = 0
dragonChoice = None


hasGUN =False
haswoodenSword = False
hasmilk = False
hasbottle = False

def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

haswoodenSword = False
damage = random.randint(1,100)
pickUpItem = input("you see a wood sword on the ground. Do you think it will help? Type sure or nope then press enter.\n")
if pickUpItem == "sure":
    haswoodenSword = True

if haswoodenSword:
    damage += 17
else:
    damage += 4

hasmilk = False
healing = random.randint(-100,1)
pickUpItem = input("you see milk on the ground. Do you think it will help? Type sure or nope then press enter.\n")
if pickUpItem == "sure":
    hasmilk = True

if hasmilk:
    healing += -500
else:
    damage += 4


hasGUN = False
damage = random.randint(1,100)
pickUpItem = input("you see a GUN on the ground. it will help... Type sure then press enter.\n")
if pickUpItem == "sure":
    hasGUN = True

if hasGUN:
    damage += 1000000
else:
    damage += 4

print(f"Hello you have chose {haswoodenSword}!\n")
isCorrect = input ("Is that correct? Type yes or no and press enter.\n").lower()


if isCorrect == "yes":
    print("pick where we your going!\n")
#else:
    

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')

if   yourChoice == "attack" and dragonChoice == "defence":
    
        yourHealth -= 1
        dragonHealth -= 4
       
elif yourChoice == "attack"and dragonChoice == "blocked":
        print(f"The Dragon chose {dragonChoice} and you chose {yourChoice}\n")
        print("The dragon blocked\n")
        yourHealth -= 1
        dragonHealth -= 4
elif yourChoice == "attack"and dragonChoice == "attack":
        print(f"The Dragon chose {dragonChoice} and you chose {yourChoice}\n")
        print("you clashed and both took massive damage\n")
        yourHealth -= 25
        dragonHealth -= 17
elif yourChoice == "blocked"and dragonChoice == "attack":
        print(f"The Dragon chose {dragonChoice} and you chose {yourChoice}\n")
        print("you blocked but took damage\n")
        yourHealth -= 8
        dragonHealth -= 8
elif yourChoice == "blocked"and dragonChoice == "blocked":
        print(f"The Dragon chose {dragonChoice} and you chose {yourChoice}\n")
        print("you both blocked what did you think would happen?\n")
        yourHealth -= 0
        dragonHealth -= 0
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


haswoodenSword = False
damage = random.randint(1,100)
pickUpItem = input("you see a wood sword on the ground. Do you think it will help? Type sure or nope then press enter.")
if pickUpItem == "sure":
    haswoodenSword = True

if haswoodenSword:
    damage += 17
else:
    damage += 4





