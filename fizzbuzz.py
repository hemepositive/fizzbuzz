# The basic FizzBuzz

def fizzbuzz():
    for x in range(1, 101):
    	#print "testing: {}".format(x)
        if (x % 3 == 0) and (x % 5 == 0):
            print "FizzBuzz"
        elif x % 5 == 0:
            print "Buzz"
        elif x % 3 == 0:
            print "Fizz"
        else:
            print x

fizzbuzz()