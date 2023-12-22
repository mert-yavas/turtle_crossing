from turtle import Turtle

# Starting position for the player turtle
STARTING_POSITION = (0, -280)

# Distance to move the player turtle on each step
MOVE_DISTANCE = 10

# Y-coordinate for the finish line
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Set the shape of the player turtle
        self.setheading(90)  # Set the initial orientation (facing upwards)
        self.penup()  # Lift the pen to move without drawing
        self.goto(STARTING_POSITION)  # Move to the starting position

    def move(self):
        # Move the player turtle upward by the defined distance
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finish_line(self):
        # Move the player turtle to the starting position when it reaches the finish line
        self.goto(STARTING_POSITION)
