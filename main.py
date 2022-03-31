import time
from turtle import Screen
from food import Food
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

score = 0

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")                        # input and ties to the controls for the snake
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#get snake to automatically move forwards
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect snake head with food
    if snake.head.distance(food) < 15:
        print("nom nom nom!!")
        score += 1
        food.refresh()
    


screen.exitonclick()
