""" Refactor your code once again so that the function's argument is obtained by asking the user for a number. 
Use a separate function for this. How will this affect your main routine? Where is the best place to call this function?
version 7"""

# placing data collection in fizzbuzz function but it would seem to be less modular
# than placing the data collection function in the main routine.

def fizzbuzz():
    out = []
    # data collection for user
    number = user_input()
    # test for integer
    try:
        number = int(number)
    except ValueError:
        number = get_number()
    # now fizzbuzzing
    for x in range(1, int(number) + 1):
        if (x % 3 == 0) and (x % 5 == 0):
            out.append("FizzBuzz")
        elif x % 5 == 0:
            out.append("Buzz")
        elif x % 3 == 0:
            out.append("Fizz")
        else:
            out.append(x)
    return out

def get_number():
    # test for integer loop
    while True:
        try:
            n = raw_input("please enter a number; not letters or what not! > ")
            out = int(n)
            break
        except ValueError:
            pass
    return out

def user_input():
    # get initial user input; corrections to be made by get_number()
    number = raw_input("Enter a number > ")
    return number

# main routine
if __name__ == "__main__":
    the_list = fizzbuzz()
    for entry in the_list:
        print entry