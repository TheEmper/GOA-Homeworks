from turtle import *

#we want to paint a house

#step 1: Square
speed(10)

width(7)
color("blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(180)

forward(200)
right(45)

#end of the square

#step 2: roof

color("red")

begin_fill()

forward(140)
right(90)

forward(140)

end_fill()

#end of the roof

#step 3: door

color("blue")

right(45)
forward(200)

right(90)
forward(70)

color("yellow")

begin_fill()
right(90)
forward(100)

left(90)
forward(60)

left(90)
forward(100)
end_fill()
#end of the door

#step 4: a window

color("blue")
right(90)
forward(35)


right(90)
forward(6)

color("white")
forward(54)

color("black")
begin_fill()
forward(40)

left(90)
forward(20)

left(90)
forward(40)

left(90)
forward(20)
end_fill()



exitonclick()