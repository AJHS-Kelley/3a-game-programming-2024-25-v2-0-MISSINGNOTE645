# Data Types and Operators, Calvin Young, v0.0

# Fundamental Data Types
# strings - str - sequence of letters, numbers, spaces, or other characters
# Strings in python are inside ' ' or " "
# idc if you use '' or "" just be consistent

# Boolean - bool - True or False vales.

# Float - float - any number value with a decimal, +/-

# Intergers - int - any whole number, +/-, including 0.

# Data types are stored in VARIABLES.
# A Variable is basically a bucket with a name to put data in to.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT?
# VARIABLES CANNOT START WITH A NUMBER
# camelCaseVaribleNames
# snake_case_varable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 7463267 # int data types

car_speed = 7256.45 # float data type, miles per hour

has_axe = True # boolen data type
is_purple = False # boolen data type

player_name = "Thea" # string data type
enemy_type = "Random" # string data type

# ASSIGN NEW VALUES
player_name = "Aegis"
car_speed = 76.432

# DATA TYPES CAN CHANGE, BE CAREFUL
has_axe = 7.0

#Printing Data Types
new_int = 7
new_float = 8.0
new_string = "Life"
new_bool = False

# print(type(new_int))
# print(type(new_float))
# print(type(new_string))
# print(type(new_bool))

# printing Variables to console / screen
# print(player_name)
# print(enemy_type)
# print(car_speed)
# print(has_axe)

# printing variables and expressions to console / screen
# print(high_score + 4673)
# print(7 * 4)
# print(high_score)


# PRINTING VARIABLES INSIDE OF STRINGS
# print(f"Hello {player_name}. He wont be you frind for long :) {high_score}")

# ARITHMETIC OPERATORS
my_int = 7
my_float = 7.32
my_num = 0

# addition 
my_int  = 6 + 4
my_float = 5.7 + 4.76

my_int = my_int + 5

my_num = my_int + my_float
# when you add an int and a float together, the answer becomes a float

# subtraction 
my_num = my_int - my_float
my_int = my_float -2.53

# Multiplication
my_num = my_int * my_float

# Division
my_number = my_int / my_float # frist is numerator, second num is donominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMING EVEN / ODD NUMBERS
num_students = 6
num_slices_pizza = 75

left_overs = num_slices_pizza % num_students
print(left_overs)

# EXPONENTS **
num_squared = 7 ** 2 # is the bace , 2 is the exponent 

# FLOOR-DIVISION // -- Divides, throws out and decimal.
my_num = my_int // my_float

# Addition-Assignment Operator - Mostly used for counters.
my_num = 7
my_num = my_num + 4 # Old-School Method
my_num += 1 # New Hotness
my_num *= 1
my_num /= 1

# COMPARISON OPERATORS

# IS-EQUAL-TO == Are the teo values equal to each other?
# Returns True of False based on evaluation
x = 7
# print(x == 7)

# Not-EQUAL-TO != Are the two values NOT equal?
# Returns True of False based on evalution
print(x != 3)

# GREATER-THAN / GREATER-THAN-OR-EQUAL TO
print(5 > 3) # Greater than
print(12 >= 2) # Greater than or equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
print(5 < 3) # LESS Than
print(12 <= 2) # Less Than or Equal to

# LOGICAL OPERATORS
# and -- ALL CODITTONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 37
height = 86
eye_coler = "gold"
# in order to ride the teacups, yoy must be at least 18 years old and at least 60" tall.
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eye_coler == "gold")
# # ALWAYS CHECK FOR THE MOST-LIKELY-TO BE TRUE CONDITTION FIRST!!!!!
# # print(defeated_boss == True and level > 5 and has_blue_key == True)

# # or -- AT LEAST ONE CONDITTION MUST BE TRUE FOR ENTIRE STATEMANT TO BE THERE
# print(age >= 37 or hight >= 86)
# print(age >= 37 or hight >= 86 or eye_coler == "gold")
# ALWAYS CHECK FOR THE MOST-LIKELYTO BE TRUE FOR CONDITION FIRST!!!!!
# print(defeated_boss == True or level > 5 or has_blue_key == True)

# not -- RETURNS THE OPPSITE VALUE OF THE STATEMENT.
a = 6
print(a == 6)
print(not (a == 6))
print(not (not (a == 6)))

# COMBINING LOGICAL OPERATORS
# print(a == 5 and has_key == True or is_cloud == True)
# TRUE and 

# IDENIFY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATTONS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)




















