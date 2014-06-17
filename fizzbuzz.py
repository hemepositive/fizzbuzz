"""Let's add one more function that takes two integers as arguments and returns true if the first number is 
evenly divisible by the second, otherwise it returns false. Refactor the `fizzbuzz()` 
function so that it calls this function for each scenario (e.g, multiple of 3, 5, 15, etc.) 
instead of performing the logic itself..
version 10"""

# changing to accept modulo function thing
def fizzbuzz(number=100):
    out = []
    words = {(True, True): "FizzBuzz",
             (True, False): "Fizz",
             (False, True): "Buzz",
             (False, False): False }
    for x in range(1, number + 1):
        if words[(modulor(x,3),modulor(x,5))]:
            out.append(words[(modulor(x,3),modulor(x,5))])
        else:
            out.append(x)
    """
    Another way using a dictionary

    d = {(True, True): "FizzBuzz",
         (True, False): "Fizz",
         (False, True): "Buzz"}
    for x in range(1, number + 1):
        if (modulor(x,3),modulor(x,5)) in d.keys():
            out.append(words[(modulor(x,3),modulor(x,5))])
        else:
            out.append(x)
    """
    return out

# divides to numbers and returns true if a evenly divides b
def modulor(a,b):
    if a % b == 0:
        return True
    return False


 # validation of user input
def check_for_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

# loops until user supplies something that can be "intted"
def get_integer(number):
    # test for integer loop
    while check_for_int(number) == False:
        number = raw_input("please enter a number; not letters or what not! > ")
    return int(number)

# get initial user input
def user_input():
    number = raw_input("Enter a number > ")
    return number

# main routine
if __name__ == "__main__":
    number = user_input()
    n = get_integer(number)
    the_list = fizzbuzz(n)
    for entry in the_list:
        print entry
