"""
This file is not a tree in the sense that you might think. It's actually a script that draws a random tree with turtle.
It recursively creates a tree, and was primarily a meant as a means of learning recursion. Everything about this file is highly adaptable,
including with drawing more, or less, angled trees, longer or shorter trees, or even diagramming binary trees. A bit can be learned about
turtles as well.
"""


import turtle
import random

def tree(branchLen,twide,t):
    branch_angle = random.randrange(-45,45)
    branch_len = random.randrange(5,20)

    if branchLen > 5:
        t.width(twide)
        t.forward(branchLen)
        t.right(branch_angle)
        tree(branchLen-branch_len,twide-2,t)
        t.width(twide)
        t.left(branch_angle*2)
        tree(branchLen-branch_len,twide-2,t)
        t.right(branch_angle)
        t.backward(branchLen)

    if branchLen >= 25:
        t.color('Brown')


    if branchLen < 15:
        t.color('Green')

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.color('Brown')
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(90,20,t)
    myWin.exitonclick()

main()

