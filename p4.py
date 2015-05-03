def ispalindrome(number):
	numstr = str(number)
	#[::-1] reverses a string with "extended slicing"
	if numstr == numstr[::-1]:
		return True
	else:
		return False

firstnumber = 111
secondnumber = 111
largestpalindrome = 0

#iterates first number from 111 to 999 and multiples it by iterations of the second number from 111 to 999 for each number
#if the number is a palindrome, compare it to the current largest palindrome
#if it is larger, set it as the current largest palindrome
while firstnumber <= 999:
	#reset the second number to go from 111 to 999 for each first number
	secondnumber = 111
	#loop iterating the second number
	while secondnumber <= 999:
		if ispalindrome(firstnumber * secondnumber) and largestpalindrome < firstnumber * secondnumber:
			largestpalindrome = firstnumber * secondnumber
		secondnumber = secondnumber + 1
	if ispalindrome(firstnumber * secondnumber) and largestpalindrome < firstnumber * secondnumber:
		largestpalindrome = firstnumber * secondnumber
	firstnumber = firstnumber + 1

print largestpalindrome