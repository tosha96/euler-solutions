import math

def isprime(number):
	#determines if number is prime using modulo
	divisor = 2
	#number had to be increased to 999 from 9 because the numbers got bigger, need a better solution
	if number == 1 or number == 0:
		return False
	while divisor <= math.sqrt(abs(number)):
		if number % divisor == 0 and number != divisor:
			return False
		else:
			divisor = divisor + 1
	return True

def factorial(number):
	if number == 0:
		return 1
	else:
		return number * factorial(number - 1)
