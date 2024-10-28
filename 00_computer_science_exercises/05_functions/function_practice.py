# Functions Practice, Calvin Young, v0.1

import random

def hello_world_multi(): # FUNCTION STGNATURE
    """This function will output Hello, World! in a language the user choose. """
    # print a list of languages to the screen, at least three but no more than five.
    print("""
        Welcome to the Hello, World! Translator
        Choose what language yopu would like to use.
        [A]English
        [B]Spanish
        [Y]German
        [X]Russian
        """)
    

    # allow the user to select (imput) a choice for the language.
    language = input("What language do you want?\n Pruss the button that matches the letter on the left.\n").lower()

    # print "Hello, World!" to the screen in that language.
    if language == "A":
        print("In English:\n, Hello, World!\n")
    elif language == "B":
        print("In Spanish:\n, Hola!, mondo\n")
    elif language == "C":
        print("In German:\n, Hollo Welt\n")
    elif language == "D":
            print("In Russian:\n, Privet Mir\n")
    else:
         print("In pig latin:\n, ElloHay orldway")

#hello_world_multi() # FUNCTION CALL
argument1 = random.randint(-1000, 100)

def is_even(argument1: int) -> bool: # Requires one ARGUMENT (argument1) and RETURNS a boolean value.
    """Determines if an integer value is even or odd."""
    if argument1 % 2 == 0:
        return True
    else:
        return False
    
print(is_even(argument1))

# Function with Multiple Arguments
def can_ride_roller_coaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("You can ride.\n")
        return True
    else:
        print("you cannot ride")
        return False

can_ride_roller_coaster(4,76) # Arguments must be passed in the same order in the same as the funcion signature indicates.































