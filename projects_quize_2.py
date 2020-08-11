
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
