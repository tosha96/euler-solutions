combinations = 0
total = 0

for onep in range (0,201):
	total = total + (onep*1)
	for twop in range (0,101):
		total = total + (twop*2)
		for fivep in range (0,41):
			total = total + (fivep*5)
			for tenp in range (0,21):
				total = total + (tenp*10)
				for twentyp in range (0,11):
					total = total + (twentyp*20)
					for fiftyp in range(0,5):
						total = total + (fiftyp*50)
						for onepound in range (0,3):
							total = total + (onepound*100)
							if total == 200:
								combinations += 1
							total = 0

print(combinations + 1)