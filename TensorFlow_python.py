print("Hello world Machine Learning")

def HelloWorldXY(x,y)
    if(x<10):
        print("x was <10")
     elif(x<20):
        print("x was >=10 but < 20")
    else:
        print("Hello world x > 20")
    return x + y 
for i in range(8,25,5): #i=8, 13, 18,23 (start stop stop)
    print("--- now running with i: {}".format(i))
    r = HelloWorldXY(i, i)
    print("result from hello world: {} ".format(i, r))
    
    ##doing exponential functions 
    print(3**2)
    #9
    
    #modulo operator which returns the remainder of division 
    print(9%2)
    #1
    
    #Integer division which rounds off result to the next integer
    print(7//2)
    #3
    
    
    #Hello world
print("hello world owen in |AI")

# printing shapes
print("       /  |")
print("     /    | ")
print("   /      | ")
print(" /       |")
print("/________|")

# Variables and print
char_name = "Owen"
char_age = "24"
print("my name is " + char_name + " and I am " + char_age + " years old ")

# more variables
myAge = 40
myName = "owen"
isBoyChild = True
isGirlChild = False

# next line characters and upper and lower characters
openCode = "We Learn Code here from Scratch"
print(" Owen \n The Code Ninja")
print(openCode + " for Free")
print(openCode.upper())
print(openCode.lower())
print(openCode.isupper())

# check for boolean if true or false after converting
print(openCode.upper().isupper())
print(openCode.lower().islower())

# find the length of characters and a number character and returning indexing
print(len(openCode))
print(openCode[10])
print(openCode.index("C"))

# the replace function
owenCodes = "The open Code Foundations Academy"
print(owenCodes.replace("open", "Eldoret"))

# working with numbers in python
my_Number = 20
print(2)
print(3+5)
print(-2.02)
print(4/6 + 8 *2)
print((2+6) * +6)  # Gives priority to the arithmetic operations on square
print(my_Number % 3)  # prints the remainder
print(str(my_Number))  # concerts the number into a string
print(str(my_Number) + " is my Favourite number ")  # Concatenate int with String

# Mathematical operations
my_Int = -10
print(abs(my_Int))  # absolute value
print(pow(4, 2))  # gives the absolute power of the given value
print(max(10, 60))  # returns maximum value
print(min(68, 80))
print(round(5.598))
print(floor(5.9))  # prints the lowest value
print(ceil(8.01))  # rounds off the number all times
print(sqrt(36))  # returns the square root of the number

# Getting inputs from users
name = input("Enter your name: ")
age = input("Enter your Age ")
print("Hello " + name + "! You are " + age + " Years old")

# simple Arithmetic Calculator operations
num1 = input("Enter num 1: ")
num2 = input("Enter num 2: ")
result = int(num1) + float(num2)  # int and float converts the string into integer
print(result)

# Matlip game answer
car = input("Enter your favourite car model ")
player = input("Enter your favourite football player ")
food = input("Enter your favourite food ")

print("I love driving " + car)
print("because it driven by " + player + " from Arsenal ")
print("and " + player + " loves eating " + food)


# LISTS IN PYTHON
friends = ["Owen", "Chelsea", "Timz", "Maswan", "Timothy", "Brian"]

friends[1] = "oscar" # replaces element in index 1 to oscar from Chelsea
print(friends[1])
print(friends)  # prints all elements in the list
print(friends[0])  # prints first indexed element
print(friends[-1])  # prints starting from last element
print(friends[1:])  # prints all elements emitting index 0
print(friends[1:4])  # prints between a specified range and nor 4th element

# LIST FUNCTIONS
friends = ["Owen", "Chelsea", "Timz", "Maswan", "Owen", "Timothy", "Brian"]
lucky_numbers = [1, 23, 45, 21, 16, 25, ]
friends2 = friends.copy()  # copies elements in list 1 to list 2
friends.extend(lucky_numbers)  # prints friends and added list too
friends.append("Linda")  # adds to the last item in the list
friends.insert(2, "Dakari")  # adds into a specified index
friends.remove("Owen")  # deletes Owen from the list
friends.pop()  # removes the last element in a list
friends.clear()  # deletes all the data in a list and returns an empty list
print(friends.index("Owen"))  # check if owen exists/ not by returning its index
print(friends.count("Owen"))  # returns how many times owen appears in the list
friends.sort()  # list objects in an ascending oder
lucky_numbers.reverse()  # reverses the oder of the list
print(friends)
print(lucky_numbers)
print(friends2)

# UP NEXT IS TUPLES
# TUPLES (containers for storing different types of data )
# Tuples can not be changed
coordinates = (2, 5)
print([1])  # prints tuples at index 1
print(coordinates)  # prints all the coordinates
coordinates2 = [(20, 1), (12, 8), (2, 5), (89, 100)]  # List of coordinates
print(coordinates2)  # prints all the listed coordinates


# Functions - Collections of code which performs a collection of task
def greeting_function():  # format for creating a function
    print("Hello Developer !")    # Give the instructions to the function


greeting_function()  # calling the function to execute the instructions


def function_parameter(name, age):
    print("Hello " + name + " Your age is " + str(age))


function_parameter("Owen", 32)
function_parameter("Timz ", 42)

# RETURN STATEMENTS  - returns a value to the function caller


def square(num):
    return num * num  # returns the square if a number


print("answer is " + str(square(10)))


def cube(num):
    return num * num * num  # returns the square if a number


answer = cube(3)  # introduced a variable name to store the value of function
print(answer)

# UP NEXT CONTROL STATEMENTS (IF STATEMENTS)
# If statements are used to make decision in a program

is_Developer = True
if is_Developer:
    print("Hello Developer")  # prints because the boolean is true

is_Developer = False
if is_Developer:
    print("Hello Developer")  # doesn't print because its false and not true

is_Developer = False
if is_Developer:
    print("Hello Developer")  # prints because the boolean is true
else:
    print("you are not a developer")  # prints this if the if is false

is_Developer = False
is_Designer = False
if is_Developer or is_Designer:  # Returns if either if the boolean is true
    print("Hello FullStack Developer or intermediate")  # prints because the boolean is true
else:  # returns this if all the booleans are false
    print("Hell Newbie")

is_Developer = True
is_Designer = True
if is_Developer and is_Designer:  # Returns true  if either if all the booleans are true
    print("Hello FullStack Developer")  # prints because the boolean is true
else:  # returns this if all the booleans are false
    print("You are not a developer")

# Using ElIF to draw more than two comparison
is_Developer = True
is_Designer = False
if is_Developer and is_Designer:  # Returns if either if the boolean is true
    print("Hello Full Stack Engineer !")
elif is_Developer and not(is_Designer):
    print("You are Back-End Engineer")
elif (is_Designer) and not(is_Developer):
    print("Welcome UI/Ux Engineer")
else:
    print("You are not a developer")
    
# FUNCTIONS AND COMPARISONS
# Function to return largest among three integers


def max_num(num1, num2, num3):
    if(num1 >= num2) and (num1 >= num3):
        return num1
    elif(num2 >= num1) and(num2 >= num3):
        return num2
    else:
        return num3


print(max_num(12, 30, 57))

def compare_strings(name, school, town):
    if(name == "Owen") and (school == "Kabarak") and (town == "Nakuru"):
        return True
    else:
        return False


print(compare_strings("Owen", "Kabarak", "Nakuru"))

# Using not operator !


def compare_strings(name, school, town):
    if(name != "Owen") and (school != "Kabarak") and (town != "Nakuru"):
        return True
    else:
        return False


print(compare_strings("Owen", "UOE", "Nakuru"))

# simplified Scientific Calculator combined operations
num1 = float(input("Enter Num 1: "))
operator = input("Enter operator: ")
num2 = float(input("Enter num 2: "))

if(operator == "+"):
    print(num1 + num2)
elif(operator == "/"):
    print(num1 / num2)
elif(operator == "-"):
    print(num1 - num2)
elif(operator == "*"):
    print(num1 * num2)
else:
    print("Enter correct operand")
    
 
# Dictionaries -  Used to store paired values
# Uses Key and assigned Values

weeklyDictionary = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thur": 'Thursday',
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday"
}
print(weeklyDictionary["Sun"])  # Returns error if key not found
print(weeklyDictionary.get("Wedd"))  # returns no if key not found
print(weeklyDictionary.get("Mooon", "Key not found"))  # return default instead of non

# Using Integers in dictionaries
numbersDictionary = {
    0: "False",
    1: "True",
    2: "Two",
    3: 'Three',
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}
print(numbersDictionary.get(1))  # Returns error if key not found

# WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i += 1  # or i = i +1
print("Done Looping :")


# Build a Random Picker Game
secretCode = "Python"
Guess = ""
Guess_Count = 0
Guess_Limit = 3
out_of_Guess = False
while Guess != "Python" and not(out_of_Guess):
    if Guess_Count < Guess_Limit:
        Guess = input("Enter Your Guess")
        Guess_Count += 1
    else:
        out_of_Guess = True
if out_of_Guess:
    print("Out of Guess, You Lose")
else:
    print(secretCode +  " You win !!")
    
 
# for Loop

for letter in "Computer Science":
    print(letter)

Laptops = ["Toshiba", "Hp", "Lenovo", "SamSung"]
for specs in Laptops:
    print(specs)

# print numbers between 0 and 5 but not 5
for numbers in range(5):
    print(numbers)

for index in range(5, 15):
    print(index)

# print elements in array using for loop
friends = ["Owen", "Timz", "Chelsea", "Linda", "Daktari"]
for total in range(len(friends)):
    print(friends[total])

# Combined if anf for loop logic
for i in range(5):
    if i == 0:
        print("Iteration 001")
    else:
        print("Lop not iteration 001")

# EXPONENTIAL FUNCTIONS
# prints 2 exponential 3
print(2 ** 3)

# exponential using functions


def exponential_function(base_No, pow_No):
    result = 1
    for index in range(pow_No):
        result = result * base_No
    return result


print(exponential_function(3, 3))

    
# 2D LISTS AND NESTED LOOPS
# Normal list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
print(numbers)
print(numbers[2])

# 2D List
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numbers)
# print 1 which is row 1 indexed 0 and column 1 indexed 0
print(numbers[0][0])
print(numbers[1][1])

# NESTED LOOPS
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in numbers:
    print(row)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in numbers:
    for col in row:
        print(col)

# BUILDING A WORD LANGUAGE TRANSLATOR


def translator(words):
    final_translation = ""
    for letters in words:
        if letters in "AEIOUaeiou":
            final_translation = final_translation + "g"
        else:
            final_translation = final_translation + letters
    return final_translation


print(translator(input("Enter your word to convert")))


def translator_lowercase(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            # translation = translation + "g"
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translator_lowercase(input("Enter your phrase: ")))


# UP NEXT TRY CATCH / EXCEPT ERRORS 
    
