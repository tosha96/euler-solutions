from decimal import *

#function to make a string for testing is there is only one repeating digit, recursively
def createTest(char, length, string):
	if length == 1:
		return string
	else:
		return createTest(char, length - 1, string + char)

def isOneD(string):
	#checks if result has a one-digit repeating cycle. Does not account for preceeding digits in numbers like 1/6
	for char in string:
		if createTest(str(char),len(string),"") in string:
			print createTest(str(char),len(string),"")
			return True
	return False

d = 2
bigd = 0
lcycle = 0

getcontext().prec = 3000

while d < 1000:
	string = str(Decimal(1)/Decimal(d))
	string = string[2:]
	#first and last are the first and last parts of the string seperated at k - 1 as described in wiki article
	first = string[:d-1]
	last = string[d-1:]
	#skip any non-repeating divisions
	tstring = ""
	if last != "" and not isOneD(first):
		#print d
		#need to start with smallest otherwise the repeated iterations of the cycle in the first string ruin it
		for i in range(len(first)):
			tstring = first[:i + 1]
			#print tstring
			firstremainder = first[i + 1:]
			if tstring in firstremainder:
				break
		#print len(tstring)
	if len(tstring) > lcycle:
		lcycle = len(tstring)
		bigd = d
		#print lcycle
		#print bigd
	d += 1

print lcycle
print bigd
# print Decimal(1)/Decimal(97)

#print createTest(str(2),5,"")