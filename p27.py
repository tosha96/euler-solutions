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

#print(isprime(104629))

maxprimes = 0
product = 0

for a in range(-1000,1000):
	for b in range(-1000,1000):
		n = 0
		while 1 == 1:
			result = n**2 + a*n + b
			if isprime(result):
				n += 1
			else:
				break

		if n > maxprimes:
			print("a: " + str(a))
			print("b: " + str(b))
			print("n: " + str(n))
			maxprimes = n
			product = a*b

print("Number of primes: " + str(maxprimes))
print("Product: " + str(product))
