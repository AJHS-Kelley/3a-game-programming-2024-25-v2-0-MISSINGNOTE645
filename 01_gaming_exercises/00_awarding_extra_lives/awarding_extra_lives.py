# Awarding extra lives, Calvin young, v.0.0

lives = 3
score = 100000
name = "Calvin"


print(f"Hello {name}!  you scord {score} ponits.\n")


# CHARACTER REFERENCE
# CURLY BRACES {}
# BRACKETS []
# ANGLE-BRACKETS <>
# PARENTHESES ()

# Allow user to input the score AS AN INTGER -- ADD THIS LINE OF CODE 

# If score is 10000 or less
    # Lose a life
# If score is > 10000 but less than 100001
    # Give 1 extra life
# If score is > 100000
    # Give 2 extra lives

# Output the score and number of lives the the screen

if score <= 10000:
    print("Lose a life")
    lives -= 1
elif score < 100001:
    print("Give 1 extra life")
    lives += 1
elif score > 100000:
    print("Give 2 extra lives")
    lives += 2

print("lives: " + str(lives))
print("score: " + str(score))

