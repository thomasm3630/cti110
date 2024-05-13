#Marcus Thomas
#04/28/2024
#P4 LAB1
#Use turtle and loops to draw a square and a triangle



import turtle


win = turtle.Screen()
pen = turtle.Turtle()



pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")


pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)

pen.pensize(5)
pen.pencolor("gold")
pen.shape("arrow")
pen.right(90)
pen.forward(250)
pen.right(120)
pen.forward(250)
pen.right(120)
pen.forward(250)
win.mainloop()
