# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# So far so good.  
import time
import datetime

# Initialize the game
def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

# Create the log file
logfileName = "dragonRealmLog" + str(time.time()) + ".txt"
saveData = open(logfileName, "a")
saveData.write("Game started: " + str(datetime.datetime.now()) + "\n")

# Initialize variables
numItems = 0
hasWoodenSword = False
hasMilk = False
hasGun = False
hasBottle = False
hasButterKnife = False
pathChosen = 0

# ITEM SELECTION
print("You try to go and start your quest when a text comes up: 'Please grab equipment before you leave.'\n")
print("You can pick: a bottle, a wooden sword, a box of milk, a GUN, or a butter knife.\n")
time.sleep(2)

while numItems < 2:
    selectedItem = input("Choose an item by entering its number (1: Bottle, 2: Wooden Sword, 3: Milk, 4: GUN, 5: Butter Knife): ")
    if selectedItem == "1" and not hasBottle:
        hasBottle = True
        numItems += 1
        print("why did pick a Bottle.\n")
    elif selectedItem == "2" and not hasWoodenSword:
        hasWoodenSword = True
        numItems += 1
        print("why did pick a Wooden Sword.\n")
    elif selectedItem == "3" and not hasMilk:
        hasMilk = True
        numItems += 1
        print("why did pick a Box of Milk.\n")
    elif selectedItem == "4" and not hasGun:
        hasGun = True
        numItems += 1
        print("Oh.... picked a GUN.\n")
    elif selectedItem == "5" and not hasButterKnife:
        hasButterKnife = True
        numItems += 1
        print("why did pick a Butterknife.\n")
    else:
        print("Invalid or already selected item. Please choose something else.\n")

# Display and log selected items
print("\nWell it seems you have picked your items. For some reason you decided to pick:\n")
itemsChosen = []
if hasBottle:
    print("a bottle.")
    saveData.write("The player selected a bottle.\n")
    itemsChosen.append("Bottle")
if hasWoodenSword:
    print("a wooden sword.")
    saveData.write("The player selected a wooden sword.\n")
    itemsChosen.append("Wooden Sword")
if hasMilk:
    print("a carton of milk.")
    saveData.write("The player selected a carton of milk.\n")
    itemsChosen.append("Milk")
if hasGun:
    print("a GUN.")
    saveData.write("The player selected a GUN.\n")
    itemsChosen.append("Gun")
if hasButterKnife:
    print("a butter knife.")
    saveData.write("The player selected a butter knife.\n")
    itemsChosen.append("Butter Knife")

time.sleep(3)
print("Now that you are finally done with that, choose which way to go.")

# SCENARIOS BASED ON ITEMS AND PATH CHOSEN
def forestScenario(items):
    print("\nThe forest is dense and dark, with shadows stretching long under the canopy of towering trees.")
    if "Bottle" in items and "Wooden Sword" in items:
        print("""
        A wolf lunges from the bushes. You fight it off with the sword and later gather water in the bottle to clean your wounds. 
        """)
    elif "Milk" in items and "Gun" in items:
        print("""
        A bandit tries to ambush you. You fire a warning shot, forcing them to flee. 
        You drink milk to regain your energy and press forward.
        """)
    elif "Butter Knife" in items and "Bottle" in items:
        print("""
        A snake slithers near your path. You smash it with the bottle and use the knife to skin it for food. 
        """)
    # Add combinations for remaining items if chosen

def holeScenario(items):
    print("\nYou fall into a deep hole. The air is damp, and the walls are slick.")
    if "Bottle" in items and "Milk" in items:
        print("""
        You find an underground stream and refill your bottle. The milk gives you the strength to climb out of the hole.
        """)
    elif "Gun" in items and "Butter Knife" in items:
        print("""
        A hostile creature attacks you. You fend it off with the gun and carve a torch from nearby debris using the knife. 
        """)
    # Add combinations for remaining items if chosen

def darkCaveScenario(items):
    print("\nThe cave is pitch black, with the distant sound of something breathing.")
    if "Gun" in items and "Bottle" in items:
        print("""
        A dragon blocks your path. You distract it with the bottle and escape while it's momentarily confused.
        """)
    elif "Wooden Sword" in items and "Butter Knife" in items:
        print("""
        Small creatures swarm toward you. You fend them off with the sword and use the knife to carve through a barricade.
        """)
    # Add combinations for remaining items if chosen

# PATH SELECTION
while pathChosen == 0:
    caveChosen = input("Choose your path wisely, which way will you go? Enter 1 for Forest, 2 for Hole, 3 for Dark Cave: ")

    if caveChosen == "1":
        print("\nYou venture into the forest.")
        saveData.write("Player chose the forest path.\n")
        forestScenario(itemsChosen)
        pathChosen = 1
    elif caveChosen == "2":
        print("\nYou fall into a deep hole.")
        saveData.write("Player chose the hole path.\n")
        holeScenario(itemsChosen)
        pathChosen = 2
    elif caveChosen == "3":
        print("\nYou enter the dark cave.")
        saveData.write("Player chose the dark cave path.\n")
        darkCaveScenario(itemsChosen)
        pathChosen = 3
    else:
        print("Are you just dumb... PICK ONE, TWO OR THREE YOU DUMB FU-.")


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# End of game
saveData.write("Game ended: " + str(datetime.datetime.now()) + "\n")
saveData.close()
print("\nGame data has been logged. Thank you for playing!")








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




