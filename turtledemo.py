# import turtle # turtle is a game used to play in 1960 to move left and right
# import time
#
# # noinspection PyUnresolvedReferences
# turtle.forward(150) # move in forward direction for 150 units
# # noinspection PyUnresolvedReferences
# turtle.right(250)
# turtle.forward(150)
# turtle.left(250)
# turtle.forward(150)
# turtle.left(360)
# turtle.backward(200)
# turtle.circle(50)
#
# time.sleep(10) # this is used to wait till the graphics screen closes

#### alternate method to import
from turtle import forward, right, done, backward, circle, left # this method is used to import only specific abjects
# turtle.forward(150) # move in forward direction for 150 units
done = "Bharath"
right(250) # right() is an object
forward(150)
left(250)
forward(150)
left(360)
backward(200)
circle(50)
done()
print(done)

### another way to import all objects of a module
# from turtle import * # this method is used to import all abjects
# right(250) # right() is an object
# forward(150)
# left(250)
# forward(150)
# left(360)
# circle(50)