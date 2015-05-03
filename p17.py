#dicts with word definitions
firsts = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
teens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
seconds = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

bigstring = ''

##old code that prints out number gramatically correctly

#return string of input double digit number
# def digits(s):
# 	string = ''
# 	if int(s) <= 9:
# 		string = firsts[str(int(s))]
# 	elif int(s) < 20 and int(s) > 9:
# 		string = teens[str(int(s))]
# 	else:
# 		if int(s[1]) == 0:
# 			string = seconds[str(int(s[0]))]
# 		else:
# 			string = seconds[str(int(s[0]))] + "-" + firsts[str(int(s[1]))]
# 	return string

# for counter in range(1,1001):
# 	#s = string version of current number
# 	s = str(counter)
# 	if len(s) <= 2:
# 		print digits(s)
# 	elif len(s) == 3:
# 		string = ''
# 		string = firsts[s[0]] + " hundred"
# 		lastten = s[1:]
# 		if int(lastten) > 0:
# 			string = string + " and " + digits(lastten)
# 		print string
# 	elif len(s) == 4:
# 		string = firsts[s[0]] + " thousand"
# 		print string

##final code that appends strings without spaces or dashes

#return string of input double digit number
def digits(s):
	string = ''
	if int(s) <= 9:
		string = firsts[str(int(s))]
	elif int(s) < 20 and int(s) > 9:
		string = teens[str(int(s))]
	else:
		if int(s[1]) == 0:
			string = seconds[str(int(s[0]))]
		else:
			string = seconds[str(int(s[0]))] + firsts[str(int(s[1]))]
	return string


for counter in range(1,1001):
	#s = string version of current number
	s = str(counter)
	if len(s) <= 2:
		bigstring = bigstring + digits(s)
	elif len(s) == 3:
		string = ''
		string = firsts[s[0]] + "hundred"
		lastten = s[1:]
		if int(lastten) > 0:
			string = string + "and" + digits(lastten)
		bigstring = bigstring + string
	elif len(s) == 4:
		string = firsts[s[0]] + "thousand"
		bigstring = bigstring + string

print len(bigstring)