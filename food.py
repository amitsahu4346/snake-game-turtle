from turtle import Turtle 
from random import randint
class Food:
    def __init__(self):
        self.snack = Turtle()
        self.snack.penup()
        self.snack.shape('circle')
        self.snack.color('red')
        self.snack.speed('fastest')
        self.snack.goto(randint(-280, 280),randint(-280, 280))


    def relocate(self):
        self.snack.goto(randint(-280, 280),randint(-280, 280))