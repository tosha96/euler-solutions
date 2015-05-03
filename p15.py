import random

def checkstep(position, direction):
	if direction == True and (position [0] + 1) > 6:
		return False
	elif direction == False and (position[1] - 1) < -2:
		return False
	else:
		return True

#does work for a completed step
def completestep(direction):
	if direction == True:
			position[0] = position[0] + 1
	elif direction == False:	
		position[1] = position[1] - 1
	path.append(direction)

#path is at max 4 segments long
#each segment can be either down or right
#master list of paths that paths can be checked against
paths = []
#x,y position value
position = [0,0]

path = []

#the amount of times the system has tried to create a unique path and failed. If it rises above a high enough number, we know all paths have been exhausted.
failedtries = 0

while failedtries < 100:
	#random bool, true is right and false is down
	rdirection = random.choice([True, False])
	#check if we can step anywhere
	if not checkstep(position,rdirection):
		rdirection = not rdirection
		if not checkstep(position,rdirection):
			if path in paths:
				failedtries += 1
				position = [0,0]
				path = []
			else:
				paths.append(path)
				failedtries = 0
				position = [0,0]
				path = []
		else:
			completestep(rdirection)
	else:
		completestep(rdirection)

print len(paths)

#binomial coefficient