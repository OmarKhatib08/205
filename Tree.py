# 205
#we need to input length and number of branchings

import sys

#we need turtle in order to draw
import turtle

turtle.speed(0)
turtle.left(90)

#we need to make a recursive function to draw the tree for different n
def tree(n,length,r):
    #we need a base case
    if n == 0:
        turtle.pensize(r)
        turtle.forward(length)
        turtle.backward(length)
    else:
        turtle.pensize(r)
        turtle.forward(length)
        turtle.left(40)
        tree(n-1,length/2,r/2)
        turtle.right(30)
        tree(n-1,length/3,r/2)
        turtle.right(30)
        tree(n-1,length/2,r/2)
        turtle.left(20)
        turtle.backward(length)
        

tree(4,100,10)
turtle.done()
