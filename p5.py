number = 1
divisor = 1

while 1 == 1:
	divisor = 1
	while divisor <= 20:
		if number % divisor == 0:
			divisor = divisor + 1
		else:
			break
	if divisor >= 20:
		break
	else:
		number = number + 1

print number
