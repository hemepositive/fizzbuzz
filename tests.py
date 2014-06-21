'''
from random import randint
import unittest
import mock
from fizzbuzz import fizzbuzz, user_input, modulor, validate_user_input

"""Create a separate file to test your code with unit tests.
Name this file *tests.py*. Write tests for each scenario (e.g, multiple of 3, 5, 15, etc.).
testing for version 13
Requires mock
"""

class FizzBuzzTests(unittest.TestCase):
    """ testing fizzbuzz funtion """

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

    """ testing helper funtions """

    def test_user_input(self):
        print "testing user_input"
        with mock.patch('__builtin__.raw_input', return_value=12):
            assert user_input() == 12
            print "user_input integer passed"
        with mock.patch('__builtin__.raw_input', return_value="frogs"):
            assert user_input() == "frogs"
            print "user_input string passed"

    def test_modulor(self):
        print "testing modulor"
        test_list = [[9, 3.0], [13, 3.0], [5, 5.0], [31, 5.0], [15, 3.0], [15, 5.0]]
        expected = [True, False, True, False, True, True]
        results = []
        for entry in test_list:
            results.append(modulor(entry[0], entry[1]))
        self.assertEqual(expected, results)

    def validate_user_input(self):
        print "testing validate_user_input"
        with mock.patch('__builtin__.raw_input', return_value=24):
            assert get_integer(24) == 24
            print "validate_user_input passed"

if __name__ == "__main__":
    print "testing..."
    unittest.main()
'''
