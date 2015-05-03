import math

sumofsquares = 0
squareofsums = 0
number = 1

#calculate the sum of squares
while number <= 100:
	sumofsquares = sumofsquares + number ** 2
	number = number + 1

number = 1
#calculate the square of sums
while number <= 100:
	squareofsums = squareofsums + number
	#if we have reached one hundred, get the square of the sums
	if number == 100:
		squareofsums = squareofsums ** 2
	number = number + 1

#print absolute difference between the two values
print math.fabs(sumofsquares - squareofsums)