import euler
def approxE(error):
	x = 1
	previous = 1
	current = 2

	while current - previous > error:
		x += 1
		previous,current = current, current + 1/euler.factorial(x)
	return current

print(int(approxE(0.000000000000000000000000000000000000000000000000000000000000000000000000000000001)*10000000000000000000000000000000000000000000))
