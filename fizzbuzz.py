"""Update your main routine so that you first call the function to get the value from the user. 
The return value is then passed to a function for validation, which you've already written. 
Make sure you remove the function call from `fizzbuzz()` where you first set up the validation in Step 6.
version 8"""

# stripping user_input and validation from fizzbuzz; now using main routine
def fizzbuzz(number=100):
    out = []
    for x in range(1, number + 1):
        if (x % 3 == 0) and (x % 5 == 0):
            out.append("FizzBuzz")
        elif x % 5 == 0:
            out.append("Buzz")
        elif x % 3 == 0:
            out.append("Fizz")
        else:
            out.append(x)
    return out

 # validation of user input
def validate_number(number):
    try:
        n = int(number)
    except ValueError:
        n = get_integer()
    return n

# get an integer loop
def get_integer():
    # test for integer loop
    while True:
        try:
            n = raw_input("please enter a number; not letters or what not! > ")
            out = int(n)
            break
        except ValueError:
            pass
    return out

# get initial user input
def user_input():
    number = raw_input("Enter a number > ")
    return number

# main routine
if __name__ == "__main__":
    number = user_input()
    n = validate_number(number)
    the_list = fizzbuzz(n)
    for entry in the_list:
        print entry
