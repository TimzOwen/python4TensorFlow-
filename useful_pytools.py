import random

feet_in_miles = 5000
meters_in_kilometers = 10000
beatles = ["Owen", "john", "peter", "captain"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1]


def roll_dice(num):
    return random.randint(1, num)
