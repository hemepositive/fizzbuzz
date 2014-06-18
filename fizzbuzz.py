"""Make sure you have 4 total functions that are named appropriately. 
Add docstrings to each. Make sure all your tests pass. Then PUSH your code to Github. .
version 13.
"""

# Oops I have > 4 functions; combinded 2 functions into validate_user_input
# Added docstrings

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
    for x in range(1, number + 1):
        t = (modulor(x, 3.0), modulor(x, 5.0))
        if words[t]:
            out.append(words[t])
        else:
            out.append(x)
    return out

def modulor(a,b):
    """ Takes two numbers and tests if one is
    evenly divisible by the other. Returns a bool.
    """
    s = str(float(a/b))
    cut_period = s.replace('.', ' ')
    listed = cut_period.split()
    if int(listed[-1]) == 0:
        return True
    return False


def validate_user_input(number):
    """ Funtion validates the user input and if not an integer it loops until
    an integer is entered. Returns an integer.
    """
    while True:
        try:
            x = int(number)
            return x
        except ValueError:
            number = raw_input("please enter a number; not letters or what not! > ")
            pass

def user_input():
    """ Prompts a user for a whole number.
    Returns the input which will then be validated.
    """
    number = raw_input("Enter a whole number > ")
    return number

# main routine
if __name__ == "__main__":
    number = user_input()
    n = validate_user_input(number)
    the_list = fizzbuzz(n)
    for entry in the_list:
        print entry