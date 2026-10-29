"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


# Variable global para controlar la velocidad (milisegundos de retraso)
speed_delay = 100

def accelerate():
    """Acelera la serpiente disminuyendo el retraso."""
    global speed_delay
    if speed_delay > 20:
        speed_delay -= 10

def slow_down():
    """Frena la serpiente aumentando el retraso."""
    global speed_delay
    speed_delay += 10

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
      
#  2: Atravesar los bordes (Wrapping) 
    if head.x < -200:
        head.x = 190
    elif head.x > 190:
        head.x = -200
    
    if head.y < -200:
        head.y = 190
    elif head.y > 190:
        head.y = -200

    # Validar si choca contra su propio cuerpo 
    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
        
    snake.append(head)


    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

# Funcion para mover la comida aleatoriamente.
    food.x += randrange(-1, 2) * 10
    food.y += randrange(-1, 2) * 10

    if not inside(food):
      food.x = randrange(-15, 15) * 10
      food.y = randrange(-15, 15) * 10

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()

    ontimer(move, speed_delay)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(accelerate, 'w')
onkey(slow_down, 's')
move()
done()
