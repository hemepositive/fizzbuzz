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
def check_for_int(number):
    try:
        print "check_for_int: try"
        int(number)
        print "testing {} which is a type {}.".format(number, type(number))
        return True
    except ValueError:
        print "check_for_int: except"
        return False

# get an integer loop; modified to accept argument as to make testing easier
# multiple user inputs in loop difficult to test with mock and unittest
def get_integer(number):
    # test for integer loop
    print "getting integer now"
    print "testing {} which is a type {}.".format(number, type(number))
    while check_for_int(number) == False:
        print "checked and false"
        print check_for_int(number)
        number = raw_input("please enter a number; not letters or what not! > ")
    print "now true"
    return int(number)

# get initial user input
def user_input():
    number = raw_input("Enter a number > ")
    return number

# main routine
if __name__ == "__main__":
    number = user_input()
    n = get_integer(number)
    print "testing {} which is a type {}.".format(n, type(n))
    the_list = fizzbuzz(n)
    for entry in the_list:
        print entry
