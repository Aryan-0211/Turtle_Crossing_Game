from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10 # Slow down the initial car speed
MOVE_INCREMENT = 2  # Slower increment for speed increase

class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE 
        
    def create_cars(self):
        random_chance = random.randint(1, 6)  # Lower chance to create a car (less frequent cars)
        if random_chance == 1:  # Create cars with a lower chance
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
        # Remove cars that are off-screen to keep memory usage in check
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def level_up(self):
        # Gradual speed increment to make the game challenging
        self.car_speed += MOVE_INCREMENT
