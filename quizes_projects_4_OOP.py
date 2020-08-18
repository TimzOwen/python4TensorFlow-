# OBJECT ORIENTED PROGRAMMING WITH PYTHON QUIZES AND PROJECTS:

# Declaring a class: (empty class uses pass to show it has no members or attributes)
class Fruits:
    pass

#try out this
class Apple:
    color = ""
    size = ""
    taste = ""
# assign a varibale the function to make it callable
callAple = Apple()
# now assign values to them using the .DOT notation
callAple.color = "Green"
callAple.size = "Small"
callAple.taste = "very sweet"
# print the elements
print(callAple.color, callAple.size,callAple.taste, end="")



# 1
# complete the code below to print some poems
class ___:
      color = 'unknown'

rose = Flower()
rose.color = ___

violet = ___
___

this_pun_is_for_you = ___

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)

#soln
class Flower:
      color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color="blue"

this_pun_is_for_you = "this pun is for you"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)


# 2
#Creating new instances of class objects can be a great way to keep track of values using attributes associated with 
# the object. The values of these attributes can be easily changed at the object level. The following code illustrates 
# a famous quote by George Bernard Shaw,using objects to represent people. Fill in the blanks to make the code satisfy 
# the behavior described in the quote.
# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    	___
    	return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    you.ideas ___
    me.ideas ___
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


#soln
# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    x = 0
    x=you.apples
    you.apples=me.apples
    me.apples=x
    return you.apples, me.apples

def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    x = 0
    x = you.ideas
    you.ideas += me.ideas
    me.ideas+=x

    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# 3

# The City class has the following attributes: name, country (where the city is located), elevation (measured in meters),
#  and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to
#   return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a 
#   specified minimal population. For example, 
# calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___

	#Format the return string
	if return_city.name:
		return ___
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""



#soln
# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Format the return string
    if return_city.name:
        return ("{}, {}".format(return_city.name, return_city.country))
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""


# 4
# We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following
#  the creation of each Furniture class instance, so that the describe_furniture function can format a 
# sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"

class Furniture:
    	color = ""
	material = ""

table = Furniture()
___
___

couch = Furniture()
___
___

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"


#soln
class Furniture:
    color = ""
	material = ""

table = Furniture()
table.color="brown"
table.material="wood"

couch = Furniture()
couch.color="red"
couch.material="leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"




#methods in classes Exmaple
class Animals:
    def animalSounds(self):
         print("Wouh wouh!!")
dog = Animals()
print(dog.animalSounds())


#EX 2
class Dog:
    def barking(self):
        print("Wouuh, wouuh")
lion = Dog()
print(lion.barking())

# Ex 3
class Bmw:
    def bmwType(self):
        brand="bmw3201"
        print("This brand is {}, and is the best in the market".format(brand))
brandCar = Bmw()
print(brandCar.bmwType())

#EX 4
#uses self and declared above the function to allow the member varibales to be changeable
class Bmw:
    brand = "bmw3201"
    def bmwType(self):
        print("This brand is {}, and is the best in the market".format(self.brand))
brandCar = Bmw()
print(brandCar.bmwType())
brandCar.brand = "BMWX3"
print(brandCar.bmwType())

#createing more than one instance from the same class
class Bmw:
    brand = "bmw3201"
    def bmwType(self):
        print("This brand is {}, and is the best in the market".format(self.brand))
brandCar = Bmw()
print(brandCar.bmwType())
brandCar.brand = "BMWX3"
print(brandCar.bmwType())

#Instance 2
newbrand = Bmw()
newbrand.brand = "BMWX6"
print(newbrand.bmwType())


#Return values from classes and methods
class Monkey:
    farms_attacked = 0

    def moneky_mtoto(self):
        return self.farms_attacked * 12
monkeys = Monkey()
print(monkeys.moneky_mtoto())
new_mobkey = monkeys.farms_attacked = 10
print(monkeys.moneky_mtoto())
