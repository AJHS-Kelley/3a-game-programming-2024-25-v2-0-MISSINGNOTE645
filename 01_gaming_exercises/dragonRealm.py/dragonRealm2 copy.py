# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

# Calvin you are making this entirely too complicated. 
# 

import random
import time

yourName = "test player"
yourHealth = 0
yourChoice = None

dragonHealth = 0
dragonChoice = None

kliden = False
pendragon = False


hasGUN =False
haswoodenSword = False
hasmilk = False
hasbottle = False

yourName = input("Please type your name here and press enter.\n")
print(f"Hello {yourName}!\n")
isCorrect = input ("Is that correct? Type yes or no and press enter.\n").lower()

def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()
time.sleep(3)

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
hasbottle = False
hasbottle = random.randint(1,2)
pickUpItem = input("you see a bottle on the ground. it might Type sure then press enter.\n")
if pickUpItem == "sure":
    hasbottle = True
kliden = '1'
pendragon= '1'

if kliden:
    damage += 589
elif pendragon:
    damage += 305




print(f"Hello you have chose {haswoodenSword}!\n")
isCorrect = input ("Is that correct? Type yes or no and press enter.\n").lower()

print(f"Hello you have chose {hasmilk}!\n")
isCorrect = input ("Is that correct? Type yes or no and press enter.\n").lower()

print(f"Hello you have chose {hasGUN}!\n")
isCorrect = input ("Is that correct? Type yes or no and press enter.\n").lower()

print(f"Hello you have chose {hasbottle}!\n")
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

#    friendlyCave = random.randint(1, 2)

 #   if chosenCave == str(friendlyCave):
 #       print('Gives you his treasure!')
#    yourChoice = input("Please type cave or forest press enter\n").lower()
 #   else:
 #       print('Gobbles you down in one bite!')
while yourHealth < 600 and dragonHealth < 7000:
    print(f"{yourName} you have {yourHealth} points. \nThe dragon has {dragonHealth} points\n")
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
        exit()
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()