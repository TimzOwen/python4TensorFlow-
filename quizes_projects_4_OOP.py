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



# Q5
#OK, now it’s your turn! Have a go at writing methods
# for a class. Create a Dog class with dog_years based
#  on the Piglet class shown before (one human year is about 7 dog years).
class Dog:
      years = 0
  __

fido=Dog()
fido.years=3
print(fido.dog_years())

# soln
class Dog:
   years = 0
  def dog_years(self):
    return self.years*7

fido=Dog()
fido.years=3
print(fido.dog_years())

# CONSTRUCTOR AND IMPORTANCT METHODS:
#Constructors allows us to pass in parameters directly to the instances created
#example
class Coffee:
    def __init__(self, brand, flavour):
        self.brand = brand
        self.flavour = flavour
drinkCoffee = Coffee("mac Coffee", "black")
print(drinkCoffee.brand)
print(drinkCoffee.flavour)

#Q 6:
# Want to see this in action? In this code, there's a Person class that has an attribute name,
# which gets set when constructing the object. Fill in the blanks so that 1) when an instance of the class is
# created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name.
class Person:
    def __init__(self, name):
        self.name = ___
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ___ 

# Create a new instance with a name of your choice
some_person = ___  
# Call the greeting method
print(some_person.___)

#soln 
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        user_name = ("hi, my name is {}".format(self.name))
        return user_name

# Create a new instance with a name of your choice
some_person = Person("owen")
# Call the greeting method
print(some_person.greeting())


#soln 2
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Owen")
# Call the greeting method
print(some_person.greeting())


#using __str__ to print direct out put and not storage address by computer on ommiting str conversion
class Computer:
    def __init__(self,model,storage):
        self.model =model
        self.storage=storage
    def __str__(self):
        return "Model {} had a storage of {}".format(self.model,self.storage)
pc = Computer("HP",str(10))
print(pc) # Model HP had a storga of 10


#using DocString for documenting your work. (Typing help to the funciton or methods show what it does)
>>> def to_seconds(hours, minutes, seconds):
...     """Returns the amount of seconds in the given hours, minutes and seconds."""
...     return hours*3600+minutes*60+seconds
... >>> help(to_seconds)
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes and seconds.
    
#more example
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function


# Q 7:
#write code to define an Elevator class. The elevator has a current floor, it also has a top and a bottom floor
# that are the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors requested.

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        pass
    def up(self):
        """Makes the elevator go up one floor."""
        pass
    def down(self):
        """Makes the elevator go down one floor."""
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        pass

elevator = Elevator(-1, 10, 0)

#soln
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top=top
        self.current=current
    def up(self,current):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            return self.current+1
    def down(self, bottom):
        """Makes the elevator go down one floor."""
        if self.current > self.top:
            return self.current -1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.floor=floor
        return self.floor
elevator = Elevator(-1, 10, 0)


#soln
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current=current
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            return self.current + 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current >self.bottom:
            return self.current - 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.floor <= self.top and self.floor>=self.bottom:
            return self.current = floor

elevator = Elevator(-1, 10, 0)

#soln
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current != self.top:
            return self.current + 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current != self.bottom:
            return self.current - 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        return self.current

elevator = Elevator(-1, 10, 0)

#soln 
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 10
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current == 10:
            self.current += 0
        else:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current <= -1:
            self.current -= 0
            """Makes the elevator go down one floor."""
        else:
            self.current -= 1
            
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)

elevator.up() 
elevator.current #should output 1
elevator.down() 
elevator.current #should output 0
elevator.go_to(10) 
elevator.current #should output 10


#INHERITANCE
#This allows us to reuse our code base:
#Inherits behavior from the root parent for all the siblings
class Cars:
    def __init__(self,max_speed, model):
        self.speed = max_speed
        self.model = model

#create an instance of Zubaru class
class Zubaru(Cars):
    pass
class Bmw(Cars):
    pass

zubaru_squad = Zubaru("200km/h", "Zubaru impreza")
bima_squad = Bmw("400km/hr", "BMW X6")
print(zubaru_squad.speed)
print(bima_squad.model)


#Example 2
class Animal:
    sound=""
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name = self.name, sound=self.sound))
class Piglet(Animal):
    sound = "Oink"
hamlet=Piglet("Hamlet")
print(hamlet.speak())
class Dog(Animal):
    sound = "Wouuuuuuh"
barking  = Dog("Simba")
print(barking.speak())


# Q 8
#Let’s create a new class together and inherit from it. Below we have a base class called Clothing. Together,
#let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks to make it work properly.
class Clothing:
      material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.___,self.___))
			
class Shirt(___):
  material="Cotton"


polo = Shirt("Polo")
polo.checkmaterial()


#soln
class Clothing:
    material = ""


    def __init__(self, name):
        self.name = name


    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
print(polo.checkmaterial())




#summary

#In object-oriented programming, the concept of inheritance allows you to build relationships between objects,
# grouping together similar concepts and reducing code duplication. Let's create a custom Fruit class with color and flavor attributes:
>>> class Fruit:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor


#We defined a Fruit class with a constructor for color and flavor attributes. Next, we'll define an Apple class along with a new Grape 
# class, both of which we want to inherit properties and behaviors from the Fruit class:
>>> class Apple(Fruit):
...     pass
... 
>>> class Grape(Fruit):
...     pass

# In Python, we use parentheses in the class declaration to have the class inherit from the Fruit class. So in this example,
#  we’re instructing our computer that both the Apple class and Grape class inherit from the Fruit class. This means that they
#  both have the same constructor method which sets the color and flavor attributes. We can now create instances of our Apple 
# and Grape classes:

>>> granny_smith = Apple("green", "tart")
>>> carnelian = Grape("purple", "sweet")
>>> print(granny_smith.flavor)
tart
>>> print(carnelian.color)
purple



# COMPOSITION:
#Allows you to use an instances of a class where classes are not related to each other
class Repository:
    def __init__(self):
        self.packages = {}
    def add_packages(self, package):
        self.packages[package.name]=package
    def total_size(self):
        result = 0
        for package in self.packages.value():
            result += package.size
        return result


# 9

# Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission: Finish the
# "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock.
#  When you’re finished, the script should add up to 10 cotton Polo shirts.
class Clothing:
      stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['___']:
      if item == material:
        count += Clothing.___['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


#soln
class Clothing:
      stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


# You can have a situation where two different classes are related, but there is no inheritance going on.
#  This is referred to as composition -- where one class makes use of code contained in another class.
# For example, imagine we have a Package class which represents a software package. It contains attributes
#  about the software package, like name, version, and size. We also have a Repository class which represents
# all the packages available for installation. While there’s no inheritance relationship between the two classes,
# they are related. The Repository class will contain a dictionary or
#  list of Packages that are contained in the repository. Let's take a look at an example Repository class definition:
>>> class Repository:
...      def __init__(self):
...          self.packages = {}
...      def add_package(self, package):
...          self.packages[package.name] = package
...      def total_size(self):
...          result = 0
...          for package in self.packages.values():
...              result += package.size
...          return result


