""" One potential error is that the user supplies a string instead of an integer for the `fizzbuzz()` function's argument. 
What happens in this situation? Run your code and find out. Then update your code so that if a string is supplied, 
the code enters a loop where the user is asked to supply a new number. This loop should continue to loop, 
asking for a new value, ending only when an integer is provided. 
Since this is a completely new feature, write a new function for this. This function should be called from `fizzbuzz()`.
version 6; previous tests broken now"""

# the basic fizzbuzz
def fizzbuzz():
    out = []
    number = raw_input("Enter a number > ")
    type(number)
    # test for integer
    try:
        number = int(number)
    except ValueError:
        number = get_number()
    # now fixxbuzzing
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

# main routine
if __name__ == "__main__":
    the_list = fizzbuzz()
    for entry in the_list:
        print entry