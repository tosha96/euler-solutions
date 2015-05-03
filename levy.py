import turtle

def levy(n):
	if n == 0:
		return "F"
	else:
		return "L" + levy(n-1) + "R" + levy(n-1) + "L"

def drawLevy(n,t,d):
	string = levy(n)
	for c in string:
		if c == "F":
			t.forward(d)
		elif c == "L":
			t.left(45)
		elif c == "R":
			t.right(90)

s = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
#turtle.setpos(-100,100)
turtle.pendown()
turtle.speed("fastest")

distance = 2

drawLevy(11,turtle,distance)

input()