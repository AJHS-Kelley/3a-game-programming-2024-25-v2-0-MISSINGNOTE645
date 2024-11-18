# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime

def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

# SAVEING DATA TO A FILE
# STEP 1 -- Create the file name to use.
logfileName = "dragonRealmLog" + str(time.time()) + ".txt"
# LogFileName = "dragonRealmLog.txt"
# Example: dragonRealmLog1132AM.txt

# Step 2 -- Create / Open the file to save the data.
saveData = open(logfileName, "x")
#File MODES
# "x" CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE.
# "w" CREATE FILE, IF FILE EXISts, ERASE AND OVERWRITE FILE CONTENTS.
# "A" CREATE FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.

saveData.write("game started" + " " + str(datetime.datetime.now())+ "\n")

# ITEM DATA
selectedItem = 0
numItems = 0
haswoodenSword = False
hasmilk = False
hasGUN = False
hasbottle = False
hasbutterKnife = False

# ITEM SELECTION
print("You try to go and start your quest was a text comes up 'please Grab equipment befor you leave\n")
print("you can pick: an bottle, a wood sword, a box of milk, a GUN, or a butterknife.\n")
time.sleep(4)
numItems = 0
while numItems < 2 or 1:
    selectedItem = int(input("Pick your item wisely, which will you use? Enter 1 for bottle, 2 for wooden sword, 3 for Milk 4 for GUN 5 for Butterknife"))
    if selectedItem == 1:
        hasbottle = True
    elif selectedItem == 2:
        haswoodenSword = True
    elif selectedItem == 3:
        hasmilk = True
    elif selectedItem == 4:
        hasGUN = True
    elif selectedItem == 5:
        hasbutterKnife = True
    else:
        print("Um Friend, are you ok? Its simple pick an bottle, a wood sword, a box of milk, a GUN, or a butterknife. Just do it right:/.")
        numItems += 1
    
print(" Well it seems you have picked your items. For some reason you decided to pick:\n")













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



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# CLOSE FILE
saveData.close()

