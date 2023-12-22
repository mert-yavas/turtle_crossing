from turtle import Turtle
import random

# Available colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial speed and speed increment for the cars
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []  # List to store the car objects
        self.speed = STARTING_MOVE_DISTANCE  # Initial speed of the cars

    def create_car(self):
        # Create a new car object and add it to the car list
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        x = 300
        y = random.randint(-250, 250)
        new_car.goto(x, y)
        self.car_list.append(new_car)

    def move_cars(self):
        # Move all cars in the car list forward according to their speed
        for car in self.car_list:
            car.forward(self.speed)

    def increase_speed(self):
        # Increase the speed of the cars when called
        self.speed += MOVE_INCREMENT
