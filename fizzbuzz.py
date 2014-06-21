import sys
import random

"""Make sure you have 4 total functions that are named appropriately.
Add docstrings to each. Make sure all your tests pass. Then PUSH your code to Github. .
version 13.
"""
# changelog
# 1. using xrange
# 2. more verbose variable names
# 3. intimation that user is a moron if a whole number not entered
# 4. added an exit if multiple fails to enter an integer

def fizzbuzz(number=100):
    """ Generates a list such that:
    if the number is evenly divisible by 3 it enters "Fuzz",
    is the number is evenly divisible by 5 it enters "Buzz",
    if the number is evenly divisible by 3 and 5 it enters "FizzBuzz".
    Returns a list.
    """
    out = []
    words = {(True, True): "FizzBuzz",
             (True, False): "Fizz",
             (False, True): "Buzz",
             (False, False): False }
    for num in xrange(1, number + 1):
        my_tuple = (modulor(num, 3.0), modulor(num, 5.0))
        if words[my_tuple]:
            out.append(words[my_tuple])
        else:
            out.append(num)
    return out

def modulor(a,b):
    """ Takes two numbers and tests if one is
    evenly divisible by the other. Returns a bool.
    """
    stringed_number = str(float(a/b))
    cut_period = stringed_number.replace('.', ' ')
    new_list = cut_period.split()
    if int(new_list[-1]) == 0:
        return True
    return False


def validate_user_input(test_number):
    """ Funtion validates the user input and if not an integer it loops until
    an integer is entered. Returns an integer.
    """
    attempts = 0
    messages = ["""Do you wash your face with the same water your ass is sitting in? Try a whole number this time. \nThe number keys are at the top of your keyboard.>""", "Please just enter a number. Letters are not numbers.> ",
        """You must have gone to Auburn. Whole numbers are what we are looking for. Try again.> """
        """Please for the love of all that is true and good enter an integer.> """,
        "I'm from Alabama but I know what a whole number is. Do it again.> "]
    while True:
        try:
            if attempts <=2:
                new_number = int(test_number)
                return new_number
            else:
                sys.exit("\n \n    Forget it.    \n \n")
        except ValueError:
            attempts += 1
            harsh_words = random.choice(messages)
            test_number = raw_input(harsh_words)
            pass

def user_input():
    """ Prompts a user for a whole number.
    Returns the input which will then be validated.
    """
    untested = raw_input("Enter a whole number > ")
    return untested

# main routine
if __name__ == "__main__":
    number = user_input()
    new_number = validate_user_input(number)
    the_list = fizzbuzz(new_number)
    for entry in the_list:
        print entry