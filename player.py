from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
    
    def go_up(self):
        self.forward(15)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
