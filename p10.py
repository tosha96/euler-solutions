import math

def isprime(number):
	#determines if number is prime using modulo
	divisor = 2
	#number had to be increased to 999 from 9 because the numbers got bigger, need a better solution
	if number == 1:
		return False
	while divisor <= int(math.floor(number**(1/2.0))):
		if number % divisor == 0 and number != divisor:
			return False
		else:
			divisor = divisor + 1
	return True

number = 1
primesum = 0

#loop that checks if numbers are prime and adds to the primecount if they are
while number <= 121:
	if isprime(number):
		primesum += number
		print number
	number = number + 1

print primesum
