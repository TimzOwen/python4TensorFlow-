#1.0
 #In this scenario, two friends are eating dinner at a restaurant. The bill comes in the
 #amount of 47.28 dollars. The friends decide to split the bill evenly between them, after
 #adding 15% tip for the service. Calculate the tip, the total amount to pay, and each
 #friends share, then output a message saying "Each person needs to pay: " followed by the resulting number.

bill = 47.28
tip = (bill * 0.15)
total = bill + tip
share = (total/2)
print("Each person needs to pay: " + str(share))


# Each person needs to pay: 27.186


#2.0
#This code is supposed to take two numbers, divide one by another so that the result is equal to 1,
#and display the result on the screen. Unfortunately,
#there is an error in the code. Find the error and fix it, so that the output is correct.
1234
numerator = 10
denominator = 10
result = int(numerator / denominator)
print(result)
1

# 4.0
#Combine the variables to display the sentence "How do you like Python so far?"


123456789
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " +word4 + " " +word5 +" " + word6 +" " + word7)

#How do you like Python so far?


#5.0
#This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.


print("2 + 2 = 4" )

# 5.0
#What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?

# ans: an Expression

# 6.0
#Flesh out the body of the print_seconds function so that it prints the
#total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

1234
def print_seconds(hours, minutes, seconds):
    print((hours*3600) + (minutes*60) +  seconds)

print_seconds(1,2,3)

3723

#7.0
# #Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, 
# then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.

1234567
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

11715

#8.0
#Return the time in seconds after finding the sum:
def returningSeconds(hours, miutes, seconds):
    return (hours*3600 + miutes*60 + seconds)
partA = returningSeconds(1,30,0)
partB = returningSeconds(2,60,5)
total = partA + partB
print(total)

# 9.0
# use Floor Division to calculate the seconds and hours
def calculateusingFloor(seconds):
    hours = seconds//3600
    minutes = ((seconds - (hours*3600))//60)
    seconds = (seconds - (hours*3600)-(minutes*60))
    return hours, minutes, seconds
hours, miutes,seconds = calculateusingFloor(4999)
print(hours, seconds,miutes)

# 10
#Code Reuse
# Minize the code below to make it reusable using a funcation
name = "Owen"
luckNumber=len(name) * 8
print("Hello " + name + " Your luck number is " + str(luckNumber))

name2 = "Timothy"
luckyNumber2 = len(name2) * 4
print("Hey " + name + " Your lucky number is " + str(luckyNumber2))

#minized using function:
def luckNumberMinimized(name):
    luckNo = len(name) * 8
    print("Hello " + name + " Your Lucky number today is : " + str(luckNo))
    return name
print(luckNumberMinimized("Timz"))
print(luckNumberMinimized("Timothy"))

# 10.1 
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

#expected 
def month_days(month, days):
    result = f"{month} has {days} days."
    return (result)
print (month_days("June", 30))
print (month_days("July", 31))

# 10.2
#additional
def price_check(type, price):
    oder = f"{type} costs ksh. {price} only"
    return oder
print(price_check("Toshiba", 50000))
print(price_check("Apple", 120000))

# 11. Refactor the code to make it human friendly
def calculate(d):
    q = 3.142
    z = q * (d ** 2)
    print(z)
calculate(5)
# refactored:
def areas_circle(radius):
    pi = 3.142
    area = pi * (radius ** 2)
    print(area)
areas_circle(14)

615.832

#Refactor 2
def f1(x, y):
    	z = x*y  # the area is base*height
	print("The area is " + str(z))
f1(2,5)

10

#refactored:
def rectangle_are(base, height):
    #areas is calculated by
    area = base * height
    print("The areas is " + str(area))
rectangle_are(10, 50)

500

#12
 #Let's revisit our lucky_number function. We want to change it, so that instead of printing
 #the message, it returns the message. This way, the calling line can print the message, or 
 #do something else with it if needed. Fill in the blanks to complete the code to make it work.


def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

#Hello Kay. Your lucky number is 27
#Hello Cameron. Your lucky number is 63


#13:
#This function compares two numbers and returns them in increasing order.
#Fill in the blanks, so the print statement displays the result of the function call in order.
#Hint: if a function returns multiple values, don't forget to store these values in multiple variables
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

smaller, bigger= order_numbers(100, 99)
print(smaller, bigger)

# 14. Write a program function to tell new employees that their user name must a
# at least be 3 charater for signing up.
def user_name_hint(username):
    if(len(username)<3):
        print("User name cannot be less than 3 characters")
    else:
        print("Valid User name, Welcome")
user_name_hint("Timz")

#15  check if a number id odd or positive with if;
def is_even(number):
    if(number %2 == 0):
        print("Even number")
    else:
        print("Odd number")
print(is_even(5))

#15.1 
#Use True or False boolean to check and return if a number divided by 2 has no remainder 
def is_even2(number2):
    if(number2 %2 != 0):
        return True
    return False
print(is_even2(2))

False

#16.0
# The number_group function should return "Positive" if the number received is positive, 
# #"Negative" if it's negative, and "Zero" 
# #if it's 0. Can you fill in the gaps to make that happen?

def group_function(number):
    if(number > 0):
        print(Positive)
    elif(number<0):
        print("Negaitve")
    else:
        return 0
print(group_function(6))

# 17: What's the value of this Python expression: (2**2) == 4?
False

#18:
#Complete the script by filling in the missing parts. The function receives a name, 
#then returns a greeting based on whether or not that name is "Taylor".

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))


# 19
#If a filesystem has a block size of 4096 bytes, this means that a file 
# #comprised of only one byte will still use 4096 bytes of storage. A file made 
# #up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill 
# #in the gaps in the calculate_storage function below, which calculates the total number 
# #of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks*4096)+4096
    return (full_blocks*4096)

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

#20
#Complete the function by filling in the missing parts. The color_translator function
#receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive
#primary colors (red, green, blue), so it returns "unknown" for all other colors
def color_translator(color):
    	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

# 21
# What's the value of this Python expression: "big" > "small"
True

# 22
#Students in a class receive their grades as Pass/Fail. Scores of 60 or 
#more (out of 100) mean that the grade is "Pass". For lower scores, the grade 
#is "Fail". In addition, scores above 95 (not included) are graded as "Top Score".
#Fill in this function so that it returns the proper grade.
def exam_grade(score):
    	if ((score>95)and (score<=100)):
		grade = "Top Score"
	elif ((score>=60)and (score<=95)):
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

# 23
#Complete the body of the format_name function. This function receives the
#first_name and last_name parameters and then returns a properly formatted string.
def format_name(first_name, last_name):
    	# code goes here
	if first_name!='' and last_name!='':
		return ("Name: " + last_name+", "+ first_name)
	elif first_name!='' or last_name!='':
		return ("Name: " +last_name+first_name)
	else:
			return ''
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

#25
#The longest_word function is used to compare 3 words. It should return the word with
#  the most number of characters (and the first in the list when they have the same length).
# Fill in the blank to make this happen.
def longest_word(word1, word2, word3):
    	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2)>= len(word1) and len(word2)>=(len(word3)):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# 26
#What is the output of this code?
def sum(x, y):
    		return(x+y)
print(sum(sum(1,2), sum(3,4)))  #ans 10

# 27
#What's the value of this Python expression?

((10 >= 5*2) and (10 <= 5*2)  #ans True

# 28
#The fractional_part function divides the numerator by the denominator, and returns just the fractional
# part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
#  Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 
# instead of attempting the division.
def fractional_part(numerator, denominator):
    	# Operate with numerator and denominator to 
# keep just the fractional part of the quotien
	if denominator ==0:
		return 0
	return numerator/denominator - (numerator//denominator)
	

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
