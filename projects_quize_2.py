
# 1


# Using .format

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# If the placeholders indicate a number,
# they’re replaced by the variable corresponding to that order (starting at zero).
# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""

# If the placeholders indicate a field name, they’re replaced by the variable
# corresponding to that field name. This means that parameters to format need to be passed indicating the field name.

# "{var1} {var2}".format(var1=value1, var2=value2)
"{:exp1} {:exp2}".format(value1, value2)


# If the placeholders include a colon, what comes after the colon is a
# formatting expression. See below for the expression reference

# {:d} integer value
'{:d}'.format(10.5) → '10'


# 2
# # The is_palindrome function checks if a string is a palindrome. A palindrome
#  is a string that can be equally read from left to right or right to left

# omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
#Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
def is_palindrome(input_string):
    	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for string in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if string.repla :
			new_string = ___
			reverse_string = ___
	# Compare the strings
	if ___:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

#Ans
def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for string in input_string.lower():
     if string.replace(" ",""):
        new_string = new_string + string
        reverse_string = string + reverse_string
    if reverse_string == new_string:
       return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

# 3
# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km",
# with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
def convert_distance(miles):
    	km = miles * 1.6 
	result = "{miles} miles equals {:.1f} km".formart(miles=miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# ans
# Fill in the gaps in the nametag function so that it uses the format method to return first_name and the 
# first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."
def nametag(first_name, last_name):
    	return("___.".format(___))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 


# 4
#The replace_ending function replaces the old string in a sentence
#with the new string, but only if the sentence ends with the old string.
#If there is more than one occurrence of the old string in the sentence,
#only the one at the end is replaced, not all of them. For example,
#replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string
#comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).
def replace_ending(sentence, old, new):
    	# Check if the old string is at the end of the sentence 
	if ___:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = ___
		new_sentence = ___
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

#ans
def replace_ending(sentence, old, new):
    if sentence.endswith(old):
    # Using i as the slicing index, combine the part
    # of the sentence up to the matched string at the
    # end with the new string
        i=len(sentence)
        l=len(old)
        new_sentence = sentence[0:i-l] + new
        return new_sentence
    return sentence
print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"

# List
list_x = ["we", "are","cooking!","some","Chapati"]

#possible operation on list like strings
print(list_x)
print(list_x[0])
print(list_x[2:])
print(list_x[1:3])
print(len(list_x))
print(type(list_x))
print("are" in type_list)

#  5
# Using the "split" string method from the preceding lesson, complete the get_word function
#  to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4)
#  should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.
def get_word(sentence, n):
    	# Only proceed if n is positive 
	if n > 0:
		words = ___
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(___)
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

#ans
def get_word(sentence, n):
    	# Only proceed if n is positive
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words
		if n <= len(words):
			return words[n-1]
	return (" ")
print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


# 6
# list operations
#add items to the list.
cars = ["BMW","BENZ","TOYOTA","IZUZU","FORD"]
cars.append("AUDI")
print(cars)
#add to at a specific index
cars.insert(1,"HONDA")
print(cars)
#remove elements
cars.remove("IZUZU")
print(cars)
#remove elements using indexes
cars.pop(4)
print(cars)
#replace elements using indexes
cars[1] = "ZUZUKI"
print(cars)

#ans
['BMW', 'BENZ', 'TOYOTA', 'IZUZU', 'FORD', 'AUDI']
['BMW', 'HONDA', 'BENZ', 'TOYOTA', 'IZUZU', 'FORD', 'AUDI']
['BMW', 'HONDA', 'BENZ', 'TOYOTA', 'FORD', 'AUDI']
['BMW', 'HONDA', 'BENZ', 'TOYOTA', 'AUDI']
['BMW', 'ZUZUKI', 'BENZ', 'TOYOTA', 'AUDI']


# 7
# The skip_elements function returns a list containing every other element from an input list, 
# starting with the first element. 
# Complete this function to do that, using the for loop to iterate through the input list.

def skip_elements(elements):
    	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for ___
		# Does this element belong in the resulting list?
		if ___
			# Add this element to the resulting list
			___
		# Increment i
		___

	return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#ans
def skip_elements(elements):
    	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for words in elements:
		# Does this element belong in the resulting list?
		if i<len(elements):
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		i+=2

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#ans 2
def skip_elements(elements):
    # Initialize variables
    i = 0
    new_list=elements[::2]
    return new_list

# Should be ['a', 'c', 'e', 'g']:
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']:
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
# Should be []:
print(skip_elements([]))



# 8

#Lists and Tuples
#EX
tuples_here = ('Computer','Department','IP')
print(type(tuples_here))

#Ex
def convert_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds_remaining = (seconds - (minutes * 60 + hours * 3600))
    return hours, minutes, seconds_remaining
result = convert_time(2000)
hours, minutes, seconds_remaining = result
print(result)
print(type(result))
print(convert_time(4000))
print(hours,minutes,seconds_remaining)

(0, 33, 20)
<class 'tuple'>
(1, 6, 40)
0 33 20


# 9
# use tuples to store information about a file: its name, its type and its size in bytes.
#Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
def file_size(file_info):
    	___, ___, ___= file_info
	return("{:.2f}".format(___ / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

# Ans
def file_size(file_info):
    name, type, size= file_info
    return("{:.2f}".format(size/ 1024))
print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

# summary
#. Strings are sequences of characters, and are immutable. Lists are sequences of elements of
#  any data type, and are mutable. The third sequence type is the tuple.
#  Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. 

#Ex
animal =["twiga","simba","lion","Giraffe","elephant"]
char = 0
for wildAnimals in animal:
    char += len(animal)
print("total animals characters : {}, and in avarage are:{}".format(char,char/len(animal)))

#using enumarate to find specific index
lecturers = ["mr Kebut", "mr Owen","Dr Maganga","Dr Rugiri","prof Wanyama","prof Chepkilot"]
for index,lecture in enumerate(lecturers):
  print("{} - {} ".format(index + 1, lecture))
  
1 - mr Kebut 
2 - mr Owen 
3 - Dr Maganga 
4 - Dr Rugiri 
5 - prof Wanyama 
6 - prof Chepkilot 


# 10
#Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements
#function to return every other element from the list, this time using the enumerate function
#to check if an element is on an even position or an odd position.
def skip_elements(elements):
    	# code goes here

	return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

#ans 1
def skip_elements(elements):
    # code goes here
    #Create an empty list
    list=[]
    #iterate through using enumarate
    for index,element in enumerate(elements):
        #check if the elements are even and proceed
        if index%2==0:
            list.append("{}".format(element))
    return list
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

#ans 2
def skip_elements(elements):
    elements = [v for i, v in enumerate(elements) if i % 2 == 0]
    return elements
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

#ans 3
def skip_elements(elements):
    # code goes here
    element = []
    for i, e in enumerate(elements):
        if i % 2 == 0:
            element.append(e)
    return element
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

# 11
#using enumerate function, create an automation email task to print emails and user names;
def full_list_emails(employees):
      #create an empaty list to store the emails
  updated_list=[]
  for names,emails in  employees:
    updated_list.append("{} <{}".format(names,emails))
  return updated_list
print(("timz@gmail.com","Timz owen"),("owen@gmail.com","Owen Gusir"))

#List Comperehesion
# 12
#Use List comprehesion in to reduce the the code to almost one line:

multiple_list = []
for x in range(1,20):
    x=x*7
    multiple_list.append(x)
print(multiple_list)

#ans
multiples = [ x*7 for x in range(1,20)]
print((multiples))

#iterate using list comprehension to find the lenght of words
coding_languages = ["Python","Java","Spring",".net","Ruby"]
leght_of_strings= [ len(coding_language) for coding_language in coding_languages]
print(leght_of_strings)

#print values of numbers between 1 and 100 and only thos deveible by 5
disivible_by_5 = [i for i in range(1,101) if i % 3 ==0]
print(disivible_by_5)

# 13 
# The odd_numbers function returns a list of odd numbers between
# 1 and n, inclusively. Fill in the blanks in the function, using list comprehension.
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
    	return [x for x in ___ if ___]
print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

#ans
def odd_numbers(n):
    	return  [ x for x in range(1,n+1) if x % 2 != 0 ]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []\

# 14

#Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
#Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
___  

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#ans
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for filename in filenames:
    if ".hpp" in filename:
        index = filename.index(".hpp")
        newfilename = filename[:index] + ".h"
    else:
        newfilename = filename
    newfilenames.append((filename,newfilename))
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#ans 2
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames=[]
for file in filenames:
    if file.endswith("hpp"):
        newfilenames.append(file.replace(".hpp",".h"))
    else:
        newfilenames.append(file)
print(newfilenames)


# 15
# The format_address function separates out parts of the address string into new strings:
# house_number and street_name, and returns: "house number X on street named Y". The
# format of the input string is: numeric house number, followed by the street name
#  which may contain numbers, but never by themselves, and could be several words long. For example, 
# "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
def format_address(address_string):
      # Declare variables
  house_number = 0
  street_name = ""
  # Separate the address string into parts
  separated_address = address_string.split()
  # Traverse through the address parts
  for address in separated_address:
    # Determine if the address part is the
    # house number or part of the street name
    if address.isnumeric():
      house_number = address
  # Does anything else need to be done 
  # before returning the result?
    else:
      street_name += address + " "
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# 16
# The highlight_word function changes the given word in a sentence to its upper-case 
# version. For example, highlight_word("Have a nice day", "nice") returns
#  "Have a NICE day". Can you write this function in just one line?
def highlight_word(sentence, word):
    	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# 
# create a function that turns text into pig latin: a simple text transformation
# that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
      say = ""
  # Separate the text into words
  words = ___
  for word in words:
    # Create the pig latin word and add it to the list
    ___
    # Turn the list back into a phrase
  return ___

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# ans


# ans
def pig_latin(text):
    say = ""
    pig_text = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1:] + word[0] + "ay"
        pig_text.append(word)
        # Turn the list back into a phrase
    return ' '.join(pig_text)
print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


# 18
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for 
# the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 
# 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x
#  or - when the permission is not granted. For example: 640 is read/write for the owner, read for the group, and no permissions
#   for the others; converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute 
#   for group and others; converted
#  to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal format into a string format.
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for ___ in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if ___ >= value:
                result += ___
                ___ -= value
            else:
                ___
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

# Ans
def octal_to_string(octal):
    permission = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]
    result = ""
    # Iterate over each of the digits in octal
    for ___ in [int(n) for n in str(octal)]:
        result += permission[___]
    return result

print(octal_to_string(755))
print(octal_to_string(644))
print(octal_to_string(750))
print(octal_to_string(600))

#ans 
def octal_to_string(octal):
       result = ""
   value_letters = [(4,"r"),(2,"w"),(1,"x")]
   # Iterate over each of the digits in octal
   for ___ in [int(n) for n in str(octal)]:
      # Check for each of the permissions values
      for value, letter in value_letters:
          if ___ >= value:
               result += letter
               ___ -= value
          else:
               result += "-"
   return result

print(octal_to_string(755))
print(octal_to_string(644))
print(octal_to_string(750))
print(octal_to_string(600))

#ans
def octal_to_string(octal):
     result = ""
 value_letters = [(4,"r"),(2,"w"),(1,"x")]
 # Iterate over each of the digits in octal
 for i in [int(n) for n in str(octal)]:
    # Check for each of the permissions values
    for value, letter in value_letters:
        if i >= value:
            result += letter
            i -= value
        else:
            result += '-'
 return result
print(octal_to_string(755))
print(octal_to_string(644))
print(octal_to_string(750))
print(octal_to_string(600))


# 19

# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name:
# member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
def group_list(group, users):
      members = ___
  return ___

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# ans
def group_list(group, users):
      members = ", ".join(users)
  return ("{}:{}".format(group,members))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


# 20

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints 
# the sentence "Guest is X years old and works as __." for each one. For example, 
# guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef.
#  Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.
def guest_list(guests):
    	for ___:
		___
		print(___.format(___))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

#ans

def guest_list(guests):
    	count = 0
	if count < 3:
		for guest in guests:
			name, age, job = guest
			print("{} is {} years old and works as {}".format(name, age, job))
			count = count + 1
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
"""


# DICTIONARIES
# store data in key and value pair
dictiona_ary = {}
<class 'dict'>

file_counts = {"jpg":12, "png":6,"csv":15,"pdf":45,"txt":2}
#add new data
file_counts["docx"] = 12
#delete data
del file_counts["txt"]
#replace with same key
file_counts[png]=12

print(file_counts)
print(file_counts["pdf"])
print("csv" in file_counts)
print("java" in file_counts) 

#output
{'jpg': 12, 'png': 12, 'csv': 15, 'pdf': 45, 'docx': 12}
45
True
False

# 21
#The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 1) 
#add an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 3) Display the new
#dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
___ # Epilogue starts on page 39
___ # Chapter 3 now starts on page 24
___ # What are the current contents of the dictionary?
___ # Is there a Chapter 5?

#ans
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"]=39 # Epilogue starts on page 39
toc["Chapter 3"]=24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

#Iterating through  a dictionary
file_extenstion ={"jpg":12, "png":6,"csv":15,"pdf":45,"txt":2}
for extension in file_extenstion:
    print(extension)

jpg
png
csv
pdf
txt
for ext,size in file_extenstion.items():
    print("There are {} files with extension of {}".format(size,ext))
#output
There are 12 files with extension of jpg
There are 6 files with extension of png
There are 15 files with extension of csv
There are 45 files with extension of pdf
There are 2 files with extension of txt

print(file_extenstion.keys())
print(file_extenstion.values())
# output
dict_keys(['jpg', 'png', 'csv', 'pdf', 'txt'])
dict_values([12, 6, 15, 45, 2])


# 22
# Complete the code to iterate through the keys 
# and values of the cool_beasts dictionary. Remember that the items 
# method returns a tuple of key, value for each element in the dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for ___ in cool_beasts.items():
    print("{} have {}".format(___))
    
#ans
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beasts,tool in cool_beasts.items():
    print("{} have {}".format(beasts,tool))
octopuses have tentacles
dolphins have fins
rhinos have horns


#counting  characters in a string 
def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter]=0
        result[letter] +=1
    return result
print(count_letter("Timz owen"))
print(count_letter("Kabudaaa") )

#output 
{'T': 1, 'i': 1, 'm': 1, 'z': 1, ' ': 1, 'o': 1, 'w': 1, 'e': 1, 'n': 1}
{'K': 1, 'a': 4, 'b': 1, 'u': 1, 'd': 1}

# 23
#In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a
# list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors.
#  Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for __:
	for __:
		print("{} {}".format(__))

  #answer
  wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
count=0
for key, value in wardrobe.items():
    for i in value:
        if count <3:
          print("{} shirt".format(i))
          count+=1
    else:
        print("{} jeans".format(i))

#solution 2
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for color, clothings in wardrobe.items():
    for clothing in clothings:
        print("{} {}".format(clothing,color))

# 24
# The email_list function receives a dictionary, which contains domain names as keys, and a
# list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
    	emails = []
	for ___:
	  for user in users:
	    emails.___
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
                   "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#ans

# 25
# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong
# to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values

def groups_per_user(group_dictionary):
    	user_groups = {}
	# Go through group_dictionary
	for ___:
		# Now go through the users in the group
		for ___:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

#solution 3
def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            user_groups.setdefault(user, []).append(group)
    return user_groups
print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

#solution 3

# # 26
# Question 26
# The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.

def add_prices(basket):
    	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for ___:
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += ___
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

#ans
def add_prices(basket):
    	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for i in basket:
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += basket[i]
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
