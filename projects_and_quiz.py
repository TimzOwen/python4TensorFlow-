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
 
 
 
# 29:
#write a loop that will execute x 10 times and print the 11th result at the end
x=0
while(x<10):
    print("Still way to go x: =" + str(x))
    x=x+1
print("finally x: = " + str(x))

# 30:
# write a code using any variable to check the number of attempt a person inputs in [password] attempts
# rem to use function and good varible names
def password(attempts):
    x = 1
    while(x<attempts):
        print("Attempt number  : " + str(x))
        x+=1
    print("Please contact admin: attempts: " + str(x))
password(6)

# Using while loop calculate the sum f numbers between 0 and 9
x = 1
sum = 0
while x<10:
    sum += x
    x+=1
print(sum)


# 31
#Fix the problrm caused by invalid answers below
def count_down(start_number):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")
count_down(3)


# 32
#figure out the problem in the infinite loop and correct
def print_range(start, end):
    	# Loop through the numbers from start to end
	n = start
	while n <= end:
            print(n)
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

#Anws 
def print_range(start, end):
    	# Loop through the numbers from start to end
	n = start
	while n <= end:
            print(n)
            n+=1
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

#33 
#write code to print_prime_factors function print all 
#the prime factors of a number. A prime factor is
#a number that is prime and divides another without a remainder.
def print_prime_factors(number):
      # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5

# 34:
#The following code can lead to an infinite loop.
#  Fix the code so that it can finish successfully for all numbers.
def is_power_of_two(n):
      # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n/2 == 1:
    return True
  return False
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

#Ans
def is_power_of_two(n):
      # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n!= 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n/2 == 1:
    return True
  return False
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

 
 
#37;
#Fcomplete the empty function so that it returns the sum of all the divisors of a number, without including it. 
# A divisor is a number that divides into another without a remainder
def sum_divisors(n):
      sum = 0
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


#Answer
def sum_divisors(n):
      x=1
  sum = 0
  if n==0:
    sum +=n
  else:
    while n > x:
      while n%x==0 and n!=x:
        sum +=x
        x+=1
      x+=1
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


#38 
#he multiplication_table function prints the results of a number passed to
#  it multiplied by 1 through 5. An additional requirement 
# is that the result is not to exceed 25, which is done with the break
#  statement. Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = ___ 
		# What is the additional condition to exit out of the loop?
		if ___ :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		___ += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

#Answer
def multiplication_table(number):
    	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number
		# What is the additional condition to exit out of the loop?
		if result>25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24



# 39 complete the code to find sum_squares
# function, so that it returns the sum of all the squares of
#  numbers between 0 and x (not included). Remember that you can
# use the range(x) function to generate a sequence of numbers from 0 to x (not included).
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in ___:
        sum += __
    return __

print(sum_squares(10)) # Should be 285

#anws:
def square(n):
    return n*n
def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum
print(sum_squares(10))

#40
#Iterate through a for loop in a list and print all your friends not less than 10 of them
friends = ['Timz', 'Owen','Chelsea','Cherono','Shem','Kiptoo','Linda','Daktari','Sean','Joy']
for team in friends:
      print("Hello Awesome :"  + team)
      

# 41:
#calculate sum of values and their length using for loop and calculate the sum and avarage:
values = [0,10,20,30,40,50,60,70,80,90,100]
sum = 0
length = 0
for value in values:
  sum += value
  length += 1
print("The sum is: " + str(sum) + " Avareg: " + (sum/length))

# 42
#calculate the factorial of a number using function:
def factorial(n):
    result = 1
    for i in range(1,(n+1)):
        result = i * result
    return result
print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

#or
def factorial(n):
    result = 1
    for x in range(result,(n+1)):
        result *= x
    return result
print(factorial(4)) #34

#43
# Using function and for loop ,create a temperature to celcius converstion that will
# convert starting at 0, end at 100 and interval of 10:
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("Temp at :" + str(x) + " is: " + str(to_celsius(x)))
 
 
#44
#create a team match for football using nested for loop.make sure there is no team that is playing
#againest itself and print the score board for the Coach;
teams = ['Chelsea', 'Arsenal','Man city', 'Man U','AFC Leopard', 'Barcelona','Liverpool']

for home_team in teams:
  for away_team in teams:
    if(home_team!=away_team):
      print("[ " + home_team + " VS " + away_team +" ]")

# 45
# using the block 7 spinner game,use for loop to interate each block and make sure  no repetition
for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]",end="")
    print()
[0|0][0|1][0|2][0|3][0|4][0|5][0|6]
[1|1][1|2][1|3][1|4][1|5][1|6]
[2|2][2|3][2|4][2|5][2|6]
[3|3][3|4][3|5][3|6]
[4|4][4|5][4|6]
[5|5][5|6]
[6|6]

# 46
#Debug and Fix the code to iterate for only one worddef validate_users(users):
for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")
validate_users("purplecat")

#solved
def validate_users(users):
      for user in users:
        if len(user)>3:
          print(user + " is valid")
      else:
       print(user + " is invalid")
validate_users(["purplecat"])


# 47
#create a  factorial function that returns the factorial of n.
#  Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer 
# and all integers before it. For example, the factorial 
# of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result *= x
    return result
for n in range(0,10):
    print(n, factorial(n))

# 48
# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
for square in range(1,11):
      squared = square **3
      print(squared)

# 49
# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any 
# numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.
for multiple in range(0,100,7):
    print(multiple, end = " \n")

# 50
# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts. Currently
# the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.
def retry(operation, attempts):
      for n in range(attempts):
       if operation():
        print("Attempt " + str(n) + " succeeded")
        break
      else:
        print("Attempt " + str(n) + " failed")
retry(create_user, 3)
retry(stop_service, 5)

# 51
# Using recursion create a function that calls itself using a factorial sample

# Using recursion create a function that calls itself using a factorial sample
def factorial(n):
    print("Factorial called with: " + str(n))
    if n < 2:
        return 1
    result = n * factorial(n-1)
    print("Returning: " + str(result) + " For factorial " + str(n))
    return result
factorial(5)

# 52
# write a function sum_positive_numbers should return the sum of all positive numbers
# between the number n received and 1.
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should
# return 1+2+3+4+5=15. Fill in the gaps to make this work:
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    print("The positive sum is for number : " + str(n))
    if n < 1:
        return 0
    total = n + sum_positive_numbers(n-1)
    return total
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be


#ans
def is_power_of(number, base):
      # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1
  result = number//base
  # Recursive case: keep dividing number by base.
  return is_power_of(result, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# 54
# The count_users function recursively counts the amount of users that belong to a group 
# in the company system, by going through each of the members of a group 
# and if one of them is a group, recursively calling the function and counting the members. 
# But it has a bug! Can you spot the problem and fix it?

def count_users(group):
      count = 0
      for member in get_members(group):
             count += 1
             if is_group(member):
                   count += count_users(member)
                   return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

#ans
def count_users(group):
      count = 0
   for member in get_members(group):
    #count += 1
    if is_group(member):
      count += count_users(member)
    else:
      count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

# 55
#Implement the sum_positive_numbers function,
#  as a recursive function that returns the sum of all positive numbers
#  between the number n received and 1. For 
# example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
      return 0
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

#ans
def sum_positive_numbers(n):
      if n < 1:
       return 0
      total_sum = n + sum_positive_numbers(n-1)
       return total_sum
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# 56
# using while loop write code to print out the numbers 1 through 7.
number = 1
while number <= 7:
	print(number, end="\n")
	number += 1

# 57
# The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.
def show_letters(word):
    	for __:
		print(__)

show_letters("Hello")
# Should print one line per letter

#ans
def show_letters(word):
    	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter

# 58
# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has
# 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
    	count = 0
	if n == 0:
	  ___
	while (___):
		count += 1
		___
	return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

#Ans
def digits(n):
    	count = 0
	if n == 1:
	  digits = int(n) + 1
	while (n>0):
		count += 1
		n = n//10 
	return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1


# 59
# This function prints out a multiplication table (where each number is the result of multiplying the first number 
# of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:
# 1 2 3
# 2 4 6
# 3 6 9

def multiplication_table(start, stop):
    	for x in ___:
		for y in ___:
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

#ans
def multiplication_table(start, stop):
    	for x in (start,stop-1,start+stop-1):
		for y in (start,stop-1,start+stop-1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above


# 60:
#The counter function counts down from start 
# to stop when start is bigger than stop, 
# and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

def counter(start, stop):
    	x = start
	if ___:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

#ans
def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1 
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x +=1
    return return_string
print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5))


# 61
#The even_numbers function returns a space-separated
#  string of all positive numbers that are divisible by 2, up to and 
# including the maximum that's passed into the function. 
# For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.
def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1 
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x +=1
    return return_string
print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5))

 
 #Dictionaries
 dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)
 

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}def displayPerson(*args):
    for i in args:
        print(i)

displayPerson(name="Emma", age="25")
