"""Create a separate file to test your code with unit tests. 
Name this file *tests.py*. Write tests for each scenario (e.g, multiple of 3, 5, 15, etc.).
version 5"""

from random import randint
import unittest
import mock
from fizzbuzz import fizzbuzz, user_input, get_integer, validate_number


class FizzBuzzTests(unittest.TestCase):
    """ testing Fizz Buzz """

    def test_threes(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            #print index, entry, "data type: ", type(entry)
            number = index + 1
            if (number % 3) == 0 and (number % 5) != 0:
                self.assertEqual(entry, "Fizz", msg="{} should be a Fizz".format(entry))

    def test_fives(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            #print index, entry, "data type: ", type(entry)
            number = index + 1
            if (number % 3) != 0 and (number % 5) == 0:
                self.assertEqual(entry, "Buzz", msg="{} should be a Buzz".format(entry))
        
    def test_fifteens(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            #print index, entry, "data type: ", type(entry)
            number = index + 1
            if (number % 3) == 0 and (number % 5) == 0:
                self.assertEqual(entry, "FizzBuzz", msg="{} should be a FizzBuzz".format(entry))

    def test_others(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            #print index, entry, "data type: ", type(entry)
            number = index + 1
            if (number % 3) != 0 and (number % 5) != 0:
                self.assertEqual(entry, number, msg="{} and {} should be equal integers".format(str(entry), str(number)))

    def test_user_input(self):
        with mock.patch('__builtin__.raw_input', return_value=12):
            assert user_input() == 12
            print "user_input integer passed"
        with mock.patch('__builtin__.raw_input', return_value="frogs"):
            assert user_input() == "frogs"
            print "user_input string passed"

    def test_get_integer(self):
        print "testing get_integer"
        with mock.patch('__builtin__.raw_input', return_value=24):
            assert get_integer() == 24
            print "get_integer integer passed"
        # cannot figure how to test for user input of a string


    def test_validate_number(self):
        test_list = ['string', 42]
        while test_list:
            item = test_list.pop()
            if type(item) == int:
                self.assertEqual(validate_number(item), item, msg="Should return an integer")
            # problem of multiple args for get_integer
            else:
                # problem of multiple args for get_integer
                pass

        
"""
 # validation of user input
def validate_number(number):
    try:
        n = int(number)
    except ValueError:
        n = get_integer()
    return n       
"""
if __name__ == "__main__":
    print "testing..."
    unittest.main()
