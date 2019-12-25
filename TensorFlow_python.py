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
    
