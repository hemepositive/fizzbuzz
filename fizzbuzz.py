""" Refactor again. This time, update the function so that instead of printing the output, 
all numbers and strings are added to a single list. Return the entire list, 
which you should then loop through within the main routine and then print the numbers.
version 4: unchanged for verison 5 testing"""

# the basic fizzbuzz with a default value of 100
def fizzbuzz(number=100):
    out = []
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

# main routine
if __name__ == "__main__":
    number = raw_input("Enter a number > ")
    the_list = fizzbuzz(number)
    for entry in the_list:
        print entry