"""Make sure you have 4 total functions that are named appropriately. 
Add docstrings to each. Make sure all your tests pass. Then PUSH your code to Github. .
version 13"""

# Oops I have > 4 functions; combinded 2 functions into validate_user_input
# Adding docstrings

def fizzbuzz(number=100):
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
    s = str(float(a/b))
    cut_period = s.replace('.', ' ')
    listed = cut_period.split()
    if int(listed[-1]) == 0:
        return True
    return False


# loops until user supplies something that can be "intted"
def validate_user_input(number):
    # test for integer loop
    while True:
        try:
            x = int(number)
            return x
        except ValueError:
            number = raw_input("please enter a number; not letters or what not! > ")
            pass

# get initial user input
def user_input():
    number = raw_input("Enter a number > ")
    return number

# main routine
if __name__ == "__main__":
    number = user_input()
    n = validate_user_input(number)
    the_list = fizzbuzz(n)
    for entry in the_list:
        print entry

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

    while check_for_int(number) == False:
        number = raw_input("please enter a number; not letters or what not! > ")
    """