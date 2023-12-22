from turtle import Turtle

# Font configuration for the scoreboard
FONT = ("arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")  # Set the color of the scoreboard text
        self.penup()  # Lift the pen to move without drawing
        self.hideturtle()  # Hide the turtle icon
        self.score = 1  # Initialize the score to 1
        self.update_scoreboard()  # Display the initial scoreboard

    def update_scoreboard(self):
        # Update and display the scores on the screen
        self.clear()  # Clear previous score display
        self.goto(-240, 270)  # Move to the specified position
        self.write(f"Level : {self.score}", align="center", font=FONT)  # Display the current score

    def point(self):
        # Increase the left player's score and update the scoreboard
        self.score += 1  # Increment the score
        self.update_scoreboard()  # Display the updated score on the scoreboard

    def game_over(self):
        # Display "GAME OVER" at the center of the screen when the game ends
        self.goto(0, 0)  # Move to the center
        self.write("GAME OVER", align="center", font=FONT)  # Display the game over message
