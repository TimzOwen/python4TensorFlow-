#Coninuation from projects quiz 2
# 27

# The format_address function separates out parts of the address string into new strings: house_number and street_name, 
# and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by
#  the street name which may contain numbers, but never by themselves, and could be several words long. For example,
#  "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
      # Declare variables

  # Separate the address string into parts

  # Traverse through the address parts
  for __:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(__)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


#ans
def format_address(address_string):
      # Declare variables
  house_number=' '
  street_name=" "

  # Separate the address string into parts
  x=address_string.split(" ")
  # Traverse through the address parts
  for y in x:
    if(y.isdigit()):
      house_number=y
    else:
      street_name+=y
      street_name+=' '
    # Determine if the address part is the
    # house number or part of the street name
 # Does anything else need to be done 
  # before returning the result?

  # Return the formatted string  
  return "house number {} on street named {}".format(house_number,street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


#soln 2
def format_address(address_string):
    num, st = address_string.split(' ',1)
    return f"house number {num} on street named {st}"
print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"


# soln3
def format_address(address_string):
      # Declare variables
  number = ''
  street = ''
  # Separate the address string into parts
  address_string = address_string.split()
  # Traverse through the address parts
  for add in address_string:
      # Determine if the address part is the
      # house number or part of the street name
      if add.isdigit():
          number += add
      # Does anything else need to be done
      # before returning the result?
      else :
          street += add
      # Return the formatted string
  return "house number {} on street named {}".format(number, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# 28

#The highlight_word function changes the given word in a sentence to its upper-case version.
#For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?
def highlight_word(sentence, word):
    	return(___)
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# soln 1
def highlight_word(sentence, word):
    	return(sentence.replace(word,word.upper()))
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# 29

# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they 
# arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the 
# class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them 
# into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. 
# Complete the steps to combine them into one list as follows:
#  the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
      # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

#soln 1
def combine_lists(list1, list2):
    	# Generate a new list containing the elements of list2
	# Followed by the elements of list1 in reverse order
	new_list=list2
	for i in reversed(range(len(list1))):
		new_list.append(list1[i])
	return new_list
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
