# create a class with the defined attributes for what you will
# want the student to contain as your defined data types .
# this is therefore the class and an object can be called with different attributes


class Students:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# class of type cars describing different cars and properties


class Cars:
    def __init__(self, made, horse_power, price, speed):
        self.made_model = made
        self.horse_power = horse_power
        self.approximate_price = price
        self.high_speed = speed
