def isprime(number):
	#determines if number is prime using modulo
	divisor = 2
	while divisor <= 9:
		if number % divisor == 0 and number != divisor or number == 1:
			return False
		else:
			divisor = divisor + 1
	return True

divisor = 2
number = 600851475143
primes = []
biggestprime = 0

while 1 == 1:
	if isprime(divisor) and number % divisor == 0 and number != divisor:
		#check that divisor is prime, that the number divides evenly by the divisor, and that the number is not the divisor
		#if these are all true, set the number to the number divided by the divisor, and add the divisor to list of primes
		primes.append(divisor)
		number = number / divisor
		#set divisor back to 2
		divisor = 2
	elif number == divisor:
		#if the number has been divided all the way down to the divisor and it is prime, add it to the list of primes and end loop
		if isprime(divisor):
			primes.append(divisor)
			break
	else:
		divisor = divisor + 1

for number in primes:
	#iterate through list of primes to find the largest one
	if number > biggestprime:
		biggestprime = number

print biggestprime
