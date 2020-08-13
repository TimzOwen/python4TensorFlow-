
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


