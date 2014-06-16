"""Create a separate file to test your code with unit tests. 
Name this file *tests.py*. Write tests for each scenario (e.g, multiple of 3, 5, 15, etc.).
version 5"""

import unittest
from fizzbuzz import fizzbuzz

 
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

if __name__ == "__main__":
	print "testing..."
	unittest.main()
