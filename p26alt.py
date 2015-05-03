import math

#https://en.wikipedia.org/wiki/Recurring_decimal
#https://en.wikipedia.org/wiki/Order_%28number_theory%29
#checks prime denominators, uses rule from wiki
def mOrder(a,n,k):
	if (a**k) % n == 1:
		return k
	else:
		return mOrder(a,n,k+1)

def isPrime(number):
	#determines if number is prime using modulo
	divisor = 2
	if number == 1:
		return False
	while divisor <= int(math.floor(number**(1/2.0))):
		if number % divisor == 0 and number != divisor:
			return False
		else:
			divisor = divisor + 1
	return True

bigd = 0
bigl = 0

for i in range(6,1000):
	if isPrime(i):
		if mOrder(10,i,2) > bigl:
			bigl = mOrder(10,i,2)
			bigd = i

print bigd
print bigl


#print mOrder(10,7,2)