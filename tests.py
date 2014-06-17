"""Create a separate file to test your code with unit tests. 
Name this file *tests.py*. Write tests for each scenario (e.g, multiple of 3, 5, 15, etc.).
version 5"""

import unittest
import mock
from fizzbuzz import fizzbuzz, user_input, get_integer, validate_number


class FizzBuzzTests(unittest.TestCase):
    """ testing Fizz Buzz """

    def test_threes(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            print index, entry, "data type: ", type(entry)
            number = index + 1
            if (number % 3) == 0 and (number % 5) != 0:
                self.assertEqual(entry, "Fizz", msg="{} should be a Fizz".format(entry))

    def test_fives(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            print index, entry, "data type: ", type(entry)
            number = index + 1
            if (number % 3) != 0 and (number % 5) == 0:
                self.assertEqual(entry, "Buzz", msg="{} should be a Buzz".format(entry))
        
    def test_fifteens(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            print index, entry, "data type: ", type(entry)
            number = index + 1
            if (number % 3) == 0 and (number % 5) == 0:
                self.assertEqual(entry, "FizzBuzz", msg="{} should be a FizzBuzz".format(entry))

    def test_others(self):
        the_list = fizzbuzz()
        for index, entry in enumerate(the_list):
            print index, entry, "data type: ", type(entry)
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

    
    def test_validate_number(self):
        pass

    def test_string_entry(self):
        pass
        

if __name__ == "__main__":
    print "testing..."
    unittest.main()

'''
import mock

def test_say_hello():
     with mock.patch('__builtin__.raw_input', return_value='dbw'):
         assert say_hello() == 'Hello dbw'

     with mock.patch('__builtin__.raw_input', side_effect=['dbw', 'uki']):
         assert say_hello() == 'Hello dbw'
         assert say_hello() == 'Hello uki'
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import unittest
from unittest.mock import patch

import question

class TestQueryYesNo(unittest.TestCase):

    @patch('__builtins__.input.return_value', 'y')
    def test_query_y(self):
        answer = question.query_yes_no("Blah?")
        self.assertTrue(answer)
'''