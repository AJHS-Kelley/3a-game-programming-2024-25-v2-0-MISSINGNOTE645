# Flow Control Structures, Ryan Kelly, v0.0
# Making Computer Programs Make Decisions

temperature = 174
color = "Gold"
height = 7
likes_pineapple_on_pizza = False

# SINGLE DECISION POINT - if STATEMENT
# if CONDITIONAL_EXPERESSION: <-- This will use a COMPARISON OPERATOR 99% of the time
    # run_this_code IF the CONDITIONAL_EXPRESSION is TRUE.  
if temperature > 100:
    print("it is as hot as the sun outside.\n")
    
if likes_pineapple_on_pizza == False:
    print("eww!?!?! Pineapple on PIZZA!!!")

# CHEAT CODE FOR IF STATEMENT THAT USE BOOLEANS
if likes_pineapple_on_pizza == False:
    print("WHY!!!")

# what if we want something different to happen?
if color == "Gold": # COMM MISTAKE FOR STUDENTS IS USING = instead of ==
    print("Your shirt is the best correct uniform color.\n")
else:
    print("Your shirt is the worst not correct unifom color\n")

if height == 5:
    print("wow your taller than alex, come on in!!!\n")
else:
    print("Take your butt back the the kitty costers\n")

# AMUSMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min, height and < max. hiight to ride.
    
if height >= 3:
    print("You're tall enough to ride my spirt spear!\n")
elif height >=6:
    print("You're to tall to ride my spirit spear get your own>:/. \n")
else: # "oh no, something's wrong!"
    print("Error, Hight not dectected. Do not ride! \n")

# When if-elif-else blocks check for the HIGHEST value first when using > or >=.
# When if-elif-else blocks check for the LOWEST value first when using < or <=.

if height <= 4:
    print("You're tall enough to ride my spirt spear!\n")
elif height < 8:
    print("You're to tall to ride my spirit spear get your own>:/. \n")
else: # "oh no, something's wrong!"
    print("Error, Hight not dectected. Do not ride! \n")

# Create an if-elif-else block thet checks for temperature.
if temperature >= 100:
    print("it's too hot outside.\n")
elif temperature >= 50:
    print("That resess is allowed.\n")
elif temperature < 50:
    print("Recess is in the GYM")
else: # no temperature detected
    print("error, Temp not detected.\n")





















