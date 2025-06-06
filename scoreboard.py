from turtle import Turtle


class ScoreBoard:
    
    def __init__(self):
        self.score = 0
        self.board = Turtle()
        self.board.color('white')
        self.board.penup()
        self.board.hideturtle()
        self.board.goto(0,260)
        self.board.write(f'Score: {self.score}', align='center', font=("Courier", 20, 'normal'))
    def game_over(self):
        self.board.goto(0,0)
        self.board.write('Game Over', align='center', font=("Courier", 20, 'normal'))
    def update_score(self):
        self.score += 1
        self.board.clear()
        self.board.write(f'Score: {self.score}', align='center', font=("Courier", 20, 'normal'))
        