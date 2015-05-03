def isprime(number):
	#determines if number is prime using modulo
	divisor = 2
	#number had to be increased to 999 from 9 because the numbers got bigger, need a better solution
	while divisor <= 999:
		if number % divisor == 0 and number != divisor or number == 1:
			return False
		else:
			divisor = divisor + 1
	return True

number = 1
primecount = 0

#loop that checks if numbers are prime and adds to the primecount if they are
while 1 == 1:
	if isprime(number):
		primecount = primecount + 1
		#once we have reached the 10,001th prime, print it and break out of the loop
		if primecount == 10001:
			print number
			break
	number = number + 1