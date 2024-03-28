import turtle
from turtle import *
# Быстрое рисование
turtle.tracer(0)
koef = 20

# Рисование фигуры
for i in range(2):
    forward(3 * koef)
    left(90)
    backward(10 * koef)
    left(90)
up()
backward(10 * koef)
right(90)
forward(8 * koef)
left(90)
down()
for i in range(2):
    forward(16 * koef)
    right(90)
    forward(8 * koef)
    right(90)

# Рисование сетки
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(5)
done()