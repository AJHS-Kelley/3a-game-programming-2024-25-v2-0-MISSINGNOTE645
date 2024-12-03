# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# So far so good.  
import time
import datetime

# Initialize the game
def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    time.sleep(2)
    print('you see three caves. In one cave there is a hole')
    time.sleep(2)
    print('then there is one that leads to a forest')
    time.sleep(2)
    print(' and lastly there is one that is just dark.....')
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
def itemSelection():
    global numItems, hasWoodenSword, hasMilk, hasGun, hasBottle, hasButterKnife
    print("You try to go and start your quest when a text comes up: 'Please grab equipment before you leave.'\n")
    time.sleep(2)
    print("You can pick: a bottle, a wooden sword, a box of milk, a GUN, or a butter knife.\n")
    time.sleep(2)

    while numItems < 2:
        selectedItem = input("Choose an item by entering its number (1: Bottle, 2: Wooden Sword, 3: Milk, 4: GUN, 5: Butter Knife): ").lower()
        if selectedItem == "1" and not hasBottle:
            hasBottle = True
            numItems += 1
            print("You picked a Bottle. This will come in handy.\n")
        elif selectedItem == "2" and not hasWoodenSword:
            hasWoodenSword = True
            numItems += 1
            print("You picked a Wooden Sword. A trusty weapon for battle.\n")
        elif selectedItem == "3" and not hasMilk:
            hasMilk = True
            numItems += 1
            print("You picked a Box of Milk. It might help you recover.\n")
        elif selectedItem == "4" and not hasGun:
            hasGun = True
            numItems += 1
            print("You picked a GUN. Powerful, but dangerous.\n")
        elif selectedItem == "5" and not hasButterKnife:
            hasButterKnife = True
            numItems += 1
            print("You picked a Butter Knife. Not very strong, but it could help in some situations.\n")
        else:
            print("Invalid or already selected item. Please choose something else.\n")

    # Display and log selected items
    print("\nWell, it seems you have picked your items. For some reason you decided to pick:\n")
    itemsChosen = []
    if hasBottle:
        print("a bottle.")
        saveData.write("You have selected a bottle.\n")
        itemsChosen.append("Bottle")
    if hasWoodenSword:
        print("a wooden sword.")
        saveData.write("You have selected a wooden sword.\n")
        itemsChosen.append("Wooden Sword")
    if hasMilk:
        print("a carton of milk.")
        saveData.write("You have selected a carton of milk.\n")
        itemsChosen.append("Milk")
    if hasGun:
        print("a GUN.")
        saveData.write("You have selected a GUN.\n")
        itemsChosen.append("Gun")
    if hasButterKnife:
        print("a butter knife.")
        saveData.write("You have selected a butter knife.\n")
        itemsChosen.append("Butter Knife")

    return itemsChosen


# SCENARIOS BASED ON ITEMS AND PATH CHOSEN
def forestScenario(items):
    print("\nThe forest is dense and dark, with shadows stretching long under the canopy of towering trees.")
    time.sleep(1)
    print("You take a deep breath and begin walking down a narrow path, the leaves crunching beneath your boots.")
    
    if "Bottle" in items and "Wooden Sword" in items:
        print("\nYou raise your wooden sword, ready to fight, but you realize the monster is too fast. You quickly grab your bottle and toss it to distract it.")
        time.sleep(2)
        print("The bottle shatters, stunning the creature for a moment. You take advantage of the opening and strike with your sword, landing a clean blow.")
        time.sleep(2)
        print("The creature stumbles back, dazed. With one final strike, you defeat it. 'That actually worked!' you think, amazed at your quick thinking.\n")
    
    elif "Milk" in items and "Gun" in items:
        print("\nYou take a deep breath and draw your gun as you hear movement in the shadows. A bandit appears!")
        time.sleep(2)
        print("You fire a warning shot, and the bandit freezes in place. You drink the milk you grabbed, feeling a rush of energy.")
        time.sleep(2)
        print("With the bandit retreating, you feel confident and ready for whatever comes next. 'That milk really did the trick,' you think.\n")

    elif "Butter Knife" in items and "Bottle" in items:
        print("\nYou’re wandering through the thick forest when a wild creature attacks! You grab your butter knife and stab it, but it’s not enough to stop the beast.")
        time.sleep(2)
        print("You throw the bottle at the creature’s head, knocking it back and giving you a chance to escape.")
        print("The creature stumbles but doesn’t follow, as you continue your journey with caution.")
        time.sleep(2)
        print("That was close, but you’re still alive.\n")

    elif "Gun" in items and "Butter Knife" in items:
        print("\nA sudden rustling in the bushes causes you to draw your gun, but a smaller creature emerges, too fast to shoot.")
        time.sleep(2)
        print("You take a quick look at your butter knife. 'Guess I’ll have to make do with this.'")
        print("With a swift strike, you disarm the creature and send it retreating, your quick thinking saving you once again.\n")

    elif "Gun" in items and "Bottle" in items:
        print("\nAs you walk through the forest, a large bear suddenly charges at you. You aim your gun and fire a warning shot.")
        time.sleep(2)
        print("The bottle you were holding falls from your hand and rolls away, but the bear seems more frightened by your gunshot than the bottle.")
        print("With one last shot, you scare the bear off, feeling a surge of relief as it runs away.\n")

    elif "Wooden Sword" in items and "Butter Knife" in items:
        print("\nA forest spirit challenges you to a duel! You draw your wooden sword and prepare for battle.")
        time.sleep(2)
        print("The spirit strikes quickly, and you manage to block its attack with your sword. In a flash of inspiration, you pull out your butter knife.")
        print("You throw the knife in a distraction, causing the spirit to falter. With one final strike from your sword, the spirit disappears.")
        print("Your quick thinking and clever use of tools saved the day.\n")

    else:
        print("\nThe dark forest feels ominous as you press onward, unsure of what dangers may lie ahead.")
        time.sleep(3)
        print("Without the right tools, you’re left to fend for yourself, but you know you’ve survived worse.")
        time.sleep(2)
        print("You hear something in the distance, but you carry on, determined to find a way out.\n")
    finalBossFight(items)

def holeScenario(items):
    print("\nYou suddenly feel the ground give way beneath your feet. You fall, tumbling down into a deep, damp hole.")
    time.sleep(1)
    print("The walls of the hole are slick with moisture, and the air is musty.")
    
    if "Bottle" in items and "Wooden Sword" in items:
        print("\nYou find yourself trapped at the bottom of a deep hole. You try to use your wooden sword to climb, but it's too slippery.")
        time.sleep(2)
        print("You look at your bottle and decide to use it to help you climb. With careful positioning, you manage to steady yourself.")
        time.sleep(2)
        print("After a struggle, you manage to use both the sword and the bottle to climb up and escape the hole. 'That was way harder than it should have been.'\n")
    
    elif "Milk" in items and "Gun" in items:
        print("\nThe hole seems endless, but you refuse to give up. You pull out your gun, using it to shoot at the rocks above, hoping for some kind of opening.")
        time.sleep(2)
        print("You drink the milk, feeling a sudden burst of energy. With newfound strength, you fire more shots, breaking free of the hole.")
        print("You make your way to freedom, feeling exhausted but victorious. 'I’ll never let myself get stuck like that again.'\n")

    elif "Butter Knife" in items and "Bottle" in items:
        print("\nAs you look around the hole, you spot a crack in the wall. You try to use your butter knife to pry the rocks apart.")
        time.sleep(2)
        print("It’s slow going, but you manage to wedge the bottle into the crack to give yourself leverage.")
        time.sleep(2)
        print("Using both items, you slowly work your way out of the hole, grateful that you didn’t give up.\n")

    elif "Gun" in items and "Butter Knife" in items:
        print("\nYou're stuck in the hole, with no way to climb up. You pull out your gun, but there’s nothing to shoot at. The butter knife doesn’t seem much help either.")
        time.sleep(2)
        print("After some thinking, you use the knife to cut some rope nearby, tying it to the gun and firing it into the surrounding rocks for leverage.")
        print("It works! You climb up using your makeshift rope. 'That was resourceful,' you think, feeling a bit proud of yourself.\n")

    elif "Gun" in items and "Bottle" in items:
        print("\nYou survey your situation. The hole is deep, but you pull out your gun and fire a shot to test the distance.")
        time.sleep(2)
        print("The bottle is your last hope. You use it to create a makeshift tool to help with climbing.")
        time.sleep(2)
        print("After a lot of effort, you finally make it to the top of the hole. You’re free, but the journey wasn’t easy.\n")

    elif "Wooden Sword" in items and "Butter Knife" in items:
        print("\nYou're stuck in the hole, and there’s no clear way out. You raise your wooden sword, trying to knock loose some rocks to create a way up.")
        time.sleep(2)
        print("You use your butter knife to scrape away some of the smaller rocks and create footholds.")
        print("With time and effort, you make it to the top. It's not glamorous, but it worked.\n")

    else:
        print("\nThe hole is a silent, oppressive place. With no tools, you’re left to wait and think of a way out.")
        time.sleep(3)
        print("Hours pass, and you finally find a weak spot in the rock walls. Using sheer willpower, you dig and claw your way to freedom.\n")
    finalBossFight(items)
    
def darkCaveScenario(items):
    print("\nThe cave is pitch black, with the distant sound of something breathing. It's eerily quiet except for the sounds of your own footsteps.")
    time.sleep(1)

    if "Bottle" in items and "Wooden Sword" in items:
        print("\nThe cave is pitch black, and you can't see anything. You pull out your wooden sword, ready to defend yourself if anything attacks.")
        time.sleep(2)
        print("You use your bottle to create a small light source, reflecting moonlight off the surface. It's weak, but it helps you move through the cave.")
        time.sleep(2)
        print("With your sword and the light from the bottle, you cautiously make your way through the cave and find the exit.\n")
    
    elif "Milk" in items and "Gun" in items:
        print("\nThe cave is so dark you can barely see your hand in front of your face. You pull out your gun, ready for anything.")
        time.sleep(2)
        print("You drink the milk, feeling a rush of energy. It gives you the focus needed to hear any movements in the darkness.")
        print("With your senses heightened, you manage to navigate the cave and eventually find a way out, taking cautious shots at any threats you encounter.\n")

    elif "Butter Knife" in items and "Bottle" in items:
        print("\nYou’re stuck in the dark cave, using your butter knife to cut through some vines and loose rock in search of a way out.")
        time.sleep(2)
        print("Using the bottle, you make a crude flashlight by reflecting light off of it, illuminating the dark corners of the cave.")
        time.sleep(2)
        print("With the combined power of your butter knife and the bottle, you finally make your way toward an exit, feeling a sense of triumph.\n")

    elif "Gun" in items and "Butter Knife" in items:
        print("\nIn the dark cave, you can’t see anything, but you can hear noises. You hold your gun tightly, listening carefully.")
        time.sleep(2)
        print("The butter knife doesn’t seem helpful in this situation, but you use it to cut through a few vines blocking your path.")
        time.sleep(2)
        print("With the gun ready and your way clear, you find your way out of the cave, relieved that you’re safe.\n")

    # Gun and Bottle scenario
    elif "Gun" in items and "Bottle" in items:
        print("\nThe cave is eerie and silent. You pull out your gun, sensing something is wrong.")
        time.sleep(2)
        print("You use the bottle to create a small but effective light source, allowing you to see the cave’s layout better.")
        time.sleep(2)
        print("With your gun drawn and the light shining, you carefully make your way through the cave, escaping its dark depths.\n")

    # Wooden Sword and Butter Knife scenario
    elif "Wooden Sword" in items and "Butter Knife" in items:
        print("\nThe cave is dark and dangerous. You draw your wooden sword, ready for anything that might jump out at you.")
        time.sleep(2)
        print("You use your butter knife to cut away any obstacles in your path, hoping it’ll be enough to make your way out.")
        time.sleep(2)
        print("After a tense journey, you finally make it out of the cave, your sword and knife your only companions in the dark.\n")

    else:
        print("\nThe cave is overwhelming. You try to find a way out, but the darkness seems to stretch on forever. It’s hard to even tell if you’re moving forward.")
        time.sleep(3)
        print("You eventually start to panic, but then you find a crack in the cave wall. With some effort, you squeeze through and escape the endless night.\n")
    finalBossFight(items) 


# FINAL BOSS FIGHT AND DIALOGUE COMBINATIONS

def finalBossFight(items):
    print("\nYou’ve made it out of the cave, forest, or hole... but now a final challenge awaits!")
    time.sleep(3)
    print("A giant creature emerges from the shadows, roaring with rage.")
    
    if  "Gun" in items and "Butter Knife" in items:
        print("\nThe boss charges at you, its eyes glowing with malice. You pull out your gun and fire a warning shot, but the creature keeps coming.")
        time.sleep(2)
        print("You fire again, hitting it in the shoulder, but the creature barely flinches. 'Of course, this is going well,' you think.")
        time.sleep(2)
        print("In desperation, you pull out your butter knife. 'This is not how I imagined my final moments,' you mutter sarcastically.")
        time.sleep(2)
        print("With a swift motion, you throw the butter knife at the creature's face. Miraculously, it distracts the boss just long enough for you to get a clean shot.")
        time.sleep(2)
        print("You pull the trigger and hit the beast in the chest. It stumbles, then collapses. 'I can’t believe that worked,' you think, bewildered.")
        time.sleep(2)
        print("You look at the butter knife on the ground. 'Who knew a kitchen utensil could be so useful in a fight?'")
    elif "Bottle" in items and "Wooden Sword" in items:
        print("\nThe boss charges at you, its massive form casting a shadow over you. You grip your wooden sword, trying to steady your nerves.")
        time.sleep(2)
        print("You dodge its first strike and swing your sword, but the beast is too quick. You stumble back, nearly losing your footing.")
        time.sleep(2)
        print("In a panic, you grab your bottle and throw it at the creature's face. The glass shatters, temporarily disorienting it.")
        time.sleep(2)
        print("Taking advantage of the opening, you swing your wooden sword with everything you have. You land a solid blow to its side.")
        time.sleep(2)
        print("The creature recoils, wounded but not defeated. It charges again, but you swing your sword one more time, this time knocking it off balance.")
        time.sleep(2)
        print("The boss stumbles, and you quickly follow up with a final strike, sending it crashing to the ground. 'I can’t believe that worked,' you mutter.")
        time.sleep(2)
        print("You stand victorious, though slightly bewildered. 'A bottle and a wooden sword? Who would have thought?'")
    elif "Gun" in items and "Bottle" in items:
        print("\nThe boss charges at you with terrifying speed. You quickly pull out your gun and aim, but the creature is fast!")
        time.sleep(2)
        print("You fire a shot, but it misses. The creature charges again, and you're forced to dodge its swipe.")
        time.sleep(2)
        print("You grab your bottle, smashing it against the creature’s face, temporarily stunning it.")
        time.sleep(2)
        print("With the creature dazed, you take another shot with your gun, hitting it squarely in the chest. The beast roars in pain.")
        time.sleep(2)
        print("The boss stumbles back, and with one final shot, you take it down. 'I didn't think this would work, but it did,' you think sarcastically.")
    elif "Bottle" in items and "Milk" in items:
        print("\nThe boss towers over you, roaring as it prepares to strike. You clutch your bottle and milk, feeling woefully underprepared.")
        time.sleep(2)
        print("As the beast lunges, you throw the bottle at its face. The glass shatters, and the liquid splashes into its eyes, blinding it temporarily.")
        time.sleep(2)
        print("The creature roars in frustration, thrashing around blindly. You take this chance to chug the milk, feeling a surge of strength and clarity.")
        time.sleep(2)
        print("With newfound energy, you grab a large rock nearby and hurl it at the creature's head, striking a critical blow.")
        time.sleep(2)
        print("The boss collapses with a final roar, defeated. You wipe your brow and mutter, 'Never underestimate the power of milk and broken glass.'")
    elif "Wooden Sword" in items and "Butter Knife" in items:
        print("\nThe boss charges toward you, its claws glinting in the dim light. You ready your wooden sword, gripping the butter knife in your other hand.")
        time.sleep(2)
        print("You block its first attack with the wooden sword, but the force sends you sliding backward. 'Great, this is going well,' you mutter.")
        time.sleep(2)
        print("The creature lunges again, and you slash at its legs with the butter knife. It's not much, but it slows the beast down.")
        time.sleep(2)
        print("You take the opening and drive your wooden sword into its side. The creature howls in pain but doesn’t fall.")
        time.sleep(2)
        print("With one last desperate charge, you stab the butter knife into its eye. The creature finally collapses.")
        time.sleep(2)
        print("'Who knew a butter knife could be so effective?' you say, catching your breath. The boss is defeated, and you're still standing.")
    elif "Milk" in items and "Gun" in items:
        print("\nThe boss charges at you with terrifying speed, its claws reaching for you. You instinctively pull out your gun and fire a warning shot.")
        time.sleep(2)
        print("The shot hits, but the creature doesn’t even flinch. You feel your pulse quicken as it gets closer. 'Great, not the response I was hoping for,' you think sarcastically.")
        time.sleep(2)
        print("In a moment of desperation, you pull out your carton of milk and take a swig. It’s strangely refreshing, and you feel a burst of energy flowing through you.")
        time.sleep(2)
        print("With newfound strength, you raise your gun and fire again, this time hitting the beast in the chest. The boss stumbles, stunned but not yet down.")
        time.sleep(2)
        print("You take another gulp of milk, the cool liquid helping you focus. The boss charges once more, but you brace yourself and fire another shot, this time landing a critical hit.")
        time.sleep(2)
        print("The creature roars, crashing to the ground, defeated. 'I can’t believe it. Milk and a gun? Who would’ve thought?' you think, panting and half in disbelief.")
    elif "Butter Knife" in items and "Bottle" in items:
        print("\nThe boss lunges toward you, its massive claws slashing through the air. You dodge to the side and draw your butter knife, barely holding it with trembling hands.")
        time.sleep(2)
        print("You realize the butter knife is not going to do much damage, but you’ve got to make it work. You look around desperately and grab your bottle, using it as a makeshift shield.")
        time.sleep(2)
        print("The creature swipes at you, but you raise the bottle just in time, the impact sending shards of glass flying, momentarily stunning the boss.")
        time.sleep(2)
        print("You take advantage of the opening and stab the butter knife into the creature’s leg. It’s not a lethal blow, but it causes the beast to stagger.")
        time.sleep(2)
        print("The creature roars in fury and charges again, but you smash the bottle over its head, shattering it. The distraction gives you just enough time to leap out of the way.")
        time.sleep(2)
        print("Finally, you make a run for it, using your butter knife to slice through the air and keep the boss at bay. It’s not graceful, but it works.")
        time.sleep(2)
        print("The creature stumbles back, defeated. You breathe a sigh of relief. 'That was way too close for comfort,' you think, glad to have survived the most ridiculous combination of items ever.")
    else:
        print("\nThe final boss approaches. You’re on the edge of defeat. You need to think fast.\n")
        print("Finally, you manage to catch it off guard and defeat it by using every last ounce of energy and wit.\n")
    
    print("Congratulations, you defeated the final boss!")


def main():
    displayIntro()  # Display introduction
    itemsChosen = itemSelection()  # Allow player to choose items
    # You can choose the path here, for example:
    pathChosen = input("Choose your path: Forest, Hole, or Dark Cave: ").lower()
    
    # Trigger different scenarios based on the chosen path
    if pathChosen == "forest":
        forestScenario(itemsChosen)
    elif pathChosen == "hole":
        holeScenario(itemsChosen)
    elif pathChosen == "dark cave":
        darkCaveScenario(itemsChosen)
    else:
        print("Invalid path! Please restart the game and choose a valid path.")
        return  # Exit the game if invalid path is chosen.

if __name__ == "__main__":
    main()

    








#def chooseCave()):
#    cave = ''
#    while cave != '1' and cave != '2':
#       print('Which cave will you go into? (1 or 2)')
#       cave = input()
#    return cave

#def checkCave(chosenCave):
 #   print('You approach the cave...')
 #   time.sleep(2)
 #   print()'It is dark and spooky...')
 #   time.sleep(2)
#    print('A large dragon jumps out in front of you! He opens his jaws and...')
 #   print()
 #   time.sleep(2)

#    friendlyCave = random.randint(1, 2)

 #   if chosenCave == str(friendlyCave):
 #       print()'Gives you his treasure!')

 #   else:
 #       print()'Gobbles you down in one bite!')




