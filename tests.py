"""Create a separate file to test your code with unit tests. 
Name this file *tests.py*. Write tests for each scenario (e.g, multiple of 3, 5, 15, etc.).
testing for version 8"""

from random import randint
import unittest
import mock
from fizzbuzz import fizzbuzz, user_input, get_integer, check_for_int


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
            assert get_integer(24) == 24
            print "get_integer integer passed"

    def test_check_for_int(self):
        test_list = (1, 44, "45", 'goat', "5dew3")
        expected = [True, True, True, False, False]
        results = []
        for entry in test_list:
            results.append(check_for_int(entry))
        self.assertEqual(expected, results)

if __name__ == "__main__":
    print "testing..."
    unittest.main()
