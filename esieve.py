#find primes below limit using Eratosthenes's sieve
#Does not work, too slow
limit = 2000000
p = 2
checkednums = []
primes = []
i = 2

while p <= limit:
	if p not in primes and p not in checkednums:
		primes.append(p)
	i = 2
	while p*i <= limit:
		if p*i not in checkednums:
			checkednums.append(p*i)
		i += 1
	p += 1

print primes