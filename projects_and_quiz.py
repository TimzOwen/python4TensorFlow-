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
