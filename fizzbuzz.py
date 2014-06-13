"""Refactor the code so that it uses a function, called `fizzbuzz()`, that takes a number as its argument. 
Then use this argument as the upper limit of the range. So, instead of a range from 1 to 100, 
the range starts at 1 and ends at the user-supplied number. Make sure to provide a 
`if __name__ == '__main__':`."""


def fizzbuzz(n=100):
	for x in range(1, n + 1):
		if (x%3==0) and (x%5==0):
			result = "Fizz Buzz"
		elif (x%5==0):
			result = "Buzz"
		elif (x%3==0):
			result = "Fizz"
		else:
			result = x
		print result

if __name__ ==  "__main__":
    number = raw_input("Enter a number > ")
    out = fizzbuzz(int(number))