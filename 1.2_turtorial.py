'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle #This program makes a minecraft cube.

draw = turtle.Turtle()
draw.speed(8)

draw.penup()
draw.goto(-25,190)
draw.write("Nice Block")
draw.goto(0,0)
draw.pendown() #Make the Nice block text and rtc

draw.begin_fill() #make right side of block
draw.fillcolor("#834217")
draw.goto(0,-150)
draw.goto(130,-100)
draw.goto(130,50)
draw.goto(0,0)
draw.end_fill()

draw.begin_fill() #make left side of block
draw.fillcolor("#834217")
draw.goto(0,-150)
draw.goto(-130,-100)
draw.goto(-130,50)
draw.goto(0,0)
draw.end_fill()

draw.penup()

draw.goto(-130,50)
draw.pendown()

draw.begin_fill() #make top side of block
draw.fillcolor("#0c832c")
draw.goto(0,100)
draw.goto(130,50)
draw.goto(0,0)
draw.end_fill()

draw.begin_fill() #Add side growth
draw.goto(0,-20)
draw.goto(130,30)
draw.goto(130,50)
draw.goto(0,0)
draw.end_fill()

draw.begin_fill() #Add side growth
draw.goto(0,-20)
draw.goto(-130,30)
draw.goto(-130,50)
draw.goto(0,0)
draw.end_fill()

draw.penup()
draw.goto(0,20) #goto bottom of next cube

draw.pendown() #make right side of small cube
draw.begin_fill()
draw.fillcolor("#834217")
draw.goto(90,55)
draw.goto(90,160)
draw.goto(0,125)
draw.goto(0,20)
draw.end_fill()

draw.begin_fill() #make left side of small cube
draw.fillcolor("#834217")
draw.goto(-90,55)
draw.goto(-90,160)
draw.goto(0,125)
draw.goto(0,20)
draw.end_fill()
draw.goto(0,125) #rtc

draw.begin_fill() #make top side of small cube
draw.fillcolor("#0c832c")
draw.goto(-90,160)
draw.goto(0,190)
draw.goto(90,160)
draw.goto(0,125) #rtc
draw.end_fill()

draw.begin_fill() #make green side of small cube
draw.goto(0,110)
draw.goto(-90,145)
draw.goto(-90,160)
draw.goto(0,125)
draw.end_fill()

draw.begin_fill() #make green side of small cube
draw.goto(0,110)
draw.goto(90,145)
draw.goto(90,160)
draw.goto(0,125)
draw.end_fill()

draw.penup()
draw.goto(130,-130)
draw.write("Daniel Mitchell")

turtle.Screen().exitonclick()
