"""Finally, you probably used the modulus operator, `%`,
to to test if a number is a multiple of 3, 5, or 15. 
Refactor your code so you are not using that operator.
version 12"""

# Changed to use method other than modulo
# I like string methods and they have not yet 
# been required in advanced fizzbuzz
# I also like my boolean tuple/dictionary method 
def fizzbuzz(number=100):
    out = []
    words = {(True, True): "FizzBuzz",
             (True, False): "Fizz",
             (False, True): "Buzz",
             (False, False): False }
    for x in range(1, number + 1):
        test3 = str(float(x/3.0))
        test5 = str(float(x/5.0))
        t = (test_for_zero(test3), test_for_zero(test5))
        if words[t]:
            out.append(words[t])
        else:
            out.append(x)
    return out

def test_for_zero(s):
    cut_period = s.replace('.', ' ')
    listed = cut_period.split()
    if int(listed[-1]) == 0:
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