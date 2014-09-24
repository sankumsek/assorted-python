import turtle
t = turtle.Turtle()
t.width(10)
for i in range (6):
	for x in ["red","gold","blue"]:
		t.color(x)
		t.circle(150)
		t.right(30)
