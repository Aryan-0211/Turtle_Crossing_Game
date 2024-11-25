import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Key listeners
screen.listen()
screen.onkey(player.go_up, "Up")

# Function to restart the game
def restart_game():
    player.go_to_start()
    car_manager.reset()
    scoreboard.reset()
    screen.update()


# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Adjust the sleep time for overall game speed
    car_manager.create_cars()  # Controlled car creation
    car_manager.move_cars()
    screen.update()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
