# Looooooooooops, Calvin Young v0.0
import random # import random module for us to use
# Generally put all your import statements

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
#while <-- Used when you do not know how many loops you'll need.

# for loop is like Go Fish, you serch each card for what the player asked
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
#"iterate through the list" means use a for loop

# for loop example -- iterating a list
# fruits = ["Apple", "banana", "starfruit", "cucumber"]
# for each_fruit in fruits:
#  print(each_fruit)

# # continue keyword -- Skips the current iteration and then finisher the loop.
# fruits = ["Apple", "banana", "starfruit", "cucumber"]
# for each_fruit in fruits:
# if each_fruit == "banana":
#       Continue
#     print(each_fruit) 

# # brake keyword -- immediately exit the loop.
# fruits = ["Apple", "banana", "starfruit", "cucumber"]
# for each_fruit in fruits:
# if each_fruit == "banana":
#       Brake
#     print(each_fruit)  

# # for loops using range(). range(x) is EXCLUSIVE, it starts at 0 and ends at x - 1 
# for i in range(100): # range 0 - 9
#     print(i)

#     # Might not always want to stary at zero.
#     for i in range(100): #
#         print(i)

# # Not want to count by 1 -- RARE
# for i in range(10, 100, 5): # 10 = start, 100 - 1 = stop, 5 = # to count by 
#     print(i) 

# # Sometimes you're not done writing the loops.
# for x in range(10):
#     pass # tells python this loops isn't finishd, dont freak out.

# while loops -- musical chairs
player_score = 0
counter = 0
while player_score < 100: # Run as long asd this is true.
    print(f"starting: {player_score}")
    player_score += random.randint(1,100)
    print(f"After: {player_score}")
    counter += 1
print(f"counter: {counter}")

