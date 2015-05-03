bigsum = 0

for i in range(1,1000001):
	powersum = 0
	for c in str(i):
		powersum += int(c)**5
	if powersum == i and i != 1:
		print(i)
		bigsum += i

print("Sum: " + str(bigsum))
