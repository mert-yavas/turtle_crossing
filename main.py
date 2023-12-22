import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic updates

# Initialize the player, car manager, and scoreboard
cem = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Set up key events
screen.listen()
screen.onkey(cem.move, "Up")

# Flag to control the game state
game_is_on = True

while game_is_on:
    time.sleep(0.1)  # Introduce a short delay for smoother gameplay
    if random.randint(1, 4) == 1:
        cars.create_car()  # Create a new car randomly
    screen.update()  # Update the screen

    if cem.ycor() == 280:
        cem.finish_line()  # Move the player to the starting position
        cars.increase_speed()  # Increase the speed of cars
        scoreboard.point()  # Increase the player's score

    for car in cars.car_list:
        if cem.distance(car) < 20:
            game_is_on = False  # End the game if the player collides with a car
            scoreboard.game_over()  # Display the game over message

    cars.move_cars()  # Move all cars on the screen

screen.exitonclick()  # Close the screen when clicked
