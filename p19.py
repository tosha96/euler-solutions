months = [31,28,31,30,31,30,31,31,30,31,30,31]
#year = 1901
sundaycount = 0
#month = 1
daynumber = 3

for year in range(1901,2001):
	for month in range(0,12):
		days = months[month]
		if month == 1:
			if year % 100 == 0:
				if year % 400 == 0:
					days = 29
			elif year % 4 == 0:
				days = 29
		# print days
		# print range(days)
		for day in range(days):
			if daynumber == 1 and day == 0:
				sundaycount += 1
				print "Sunday found!"
			if daynumber == 7:
				daynumber = 1
			else:
				daynumber += 1
			print daynumber

print sundaycount