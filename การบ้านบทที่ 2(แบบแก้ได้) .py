import turtle
import random
tao = turtle.Turtle()
color=['red','blue','yellow','green']
tao.pensize(5)

for i in range(10):
	c = random.choice(color)
	tao.color(c)
	x = random.randint(-200,200)
	y = random.randint(-200,200)
	tao.penup()
	tao.goto(x,y)
	tao.pendown()
	size = random.randint(50,100)
          
        

	for i in range(4):
	    tao.forward(size)
	    tao.left(90)

	

