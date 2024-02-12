# Etch-A-Sketch

import turtle as t

curseur = t.Turtle()
my_sc = t.Screen()

def move_f():
    curseur.forward(10)


def turn_r():
    curseur.right(5)


def turn_l():
    curseur.left(5)


def move_b():
    curseur.backward(10)


def clear():
    curseur.clear()
    curseur.penup()
    curseur.home()
    curseur.pendown()


t.title("Etche-A-Sketche")
curseur.shape("arrow")

my_sc.listen()

my_sc.onkeypress(move_f, 'Up')
my_sc.onkeypress(turn_r, 'Right')
my_sc.onkeypress(turn_l, 'Left')
my_sc.onkeypress(move_b, 'Down')
my_sc.onkeypress(clear, 'c')

my_sc.exitonclick()
