from turtle import Turtle


STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.body_parts = []
        self.create()
        self.head = self.body_parts[0]

    def add_body_part(self, position):
        self.body_part = Turtle(shape='circle')
        self.body_part.penup()
        self.body_part.color('white')
        self.body_part.goto(position)
        self.body_parts.append(self.body_part)

    def create(self):
        for position in STARTING_POSITION:
            self.add_body_part(position)
 
    def grow(self):
        self.add_body_part(self.body_parts[-1].position())



    def move(self):
        for part_num in range(len(self.body_parts)-1, 0, -1):
            x = self.body_parts[part_num - 1].xcor()
            y = self.body_parts[part_num - 1].ycor()
            self.body_parts[part_num].goto(x,y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)