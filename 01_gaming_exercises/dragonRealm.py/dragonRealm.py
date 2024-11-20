# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# So far so good.  
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
saveData = open(logfileName, "a")
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
# CAVE DATA
caveChosen = darkcave = False
pathChosen = 0
forest = False
hole = False
darkCave = False



# ITEM SELECTION
print("You try to go and start your quest was a text comes up 'please Grab equipment befor you leave\n")
print("you can pick: an bottle, a wood sword, a box of milk, a GUN, or a butterknife.\n")
time.sleep(2)
numItems = 0
while numItems < 2:
    if selectedItem == "1":
        if not hasBottle:
            hasBottle = True
            numItems += 1
            print("why did pick a Bottle.\n")
        else:
            print("You already picked a Bottle. For the love of god choose something else:/.\n")
    elif selectedItem == "2":
        if not hasWoodenSword:
            hasWoodenSword = True
            numItems += 1
            print("why did pick a Wooden Sword.\n")
        else:
            print("You already picked a Wooden Sword. For the love of god choose something else:/.\n")
    elif selectedItem == "3":
        if not hasMilk:
            hasMilk = True
            numItems += 1
            print("why did pick a Box of Milk.\n")
        else:
            print("Nice you chose Milk. Too much mink buddy.\n")
    elif selectedItem == "4":
        if not hasGUN:
            hasGUN = True
            numItems += 1
            print("Oh.... picked a GUN.\n")
        else:
            print("Uh you already picked a GUN bud.... Please choose something else.\n")
    elif selectedItem == "5":
        if not hasButterKnife:
            hasButterKnife = True
            numItems += 1
            print("why did pick a Butterknife.\n")
        else:
            print("You already picked a Butterknife. For the love of god Choose something else:/.\n")
    else:
    
        print(" Well it seems you have picked your items. For some reason you decided to pick:\n")

        if hasbottle:
            print("a bottle.")
            saveData.write ("The player selected a bottle. \n")
        if haswoodenSword:
            print("a woodenSword.")
            saveData.write("The player selected a woodenSword. \n")
        if hasmilk:
            print("a carten of milk.")
            saveData.write("The player selected carten of milk. \n")
        if hasGUN:
            print("a GUN.")
            saveData.write("The player selected a GUN. \n")
        if hasbutterKnife:
            print("a hasbutterKnife.")
            saveData.write("The player selected a hasbutterKnife. \n")
        time.sleep(3)

        print("Now you that you finally done with that chose which way to go.")


while pathChosen == 1:
    caveChosen = int(input("Chose your path wisely, which way will you go? Enter 1 for Left, 2 for Right, 3 for Forward."))
    if caveChosen == 1:
        forest = True
    elif caveChosen == 2:
        hole = True
    elif caveChosen == 3:
        darkCave = True
    else:
        print("Are you just dumb... PICK ONE, TWO OR THREE YOU DUNB FU-.")
chosenCave = caveChosen()
if chosenCave == "1":
    alive = darkcave(hasbottle)






#def chooseCave():
#    cave = ''
#    while cave != '1' and cave != '2':
#       print('Which cave will you go into? (1 or 2)')
#       cave = input()
#    return cave

#def checkCave(chosenCave):
 #   print('You approach the cave...')
 #   time.sleep(2)
 #   print('It is dark and spooky...')
 #   time.sleep(2)
#    print('A large dragon jumps out in front of you! He opens his jaws and...')
 #   print()
 #   time.sleep(2)

#    friendlyCave = random.randint(1, 2)

 #   if chosenCave == str(friendlyCave):
 #       print('Gives you his treasure!')

 #   else:
 #       print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# CLOSE FILE
saveData.write("END OF GAME LOG\n ")
saveData.close()

