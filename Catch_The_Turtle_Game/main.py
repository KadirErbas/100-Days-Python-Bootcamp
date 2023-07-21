import turtle
from random import randint

FONT = ('Arial', 20, 'normal')


# Create and set up the turtle screen
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")

# Create the turtle object and set its initial properties
turtle_instance = turtle.Turtle()
turtle_instance.penup()
turtle_instance.speed(0)
turtle_instance.shape("turtle")
turtle_instance.color("green")

# Create and set up the turtle for displaying the score
turtle_score = turtle.Turtle()
turtle_score.hideturtle()
turtle_score.penup()
turtle_score.speed(0)
turtle_score.goto(0, turtle_screen.window_height()//2-40)
turtle_score.write(f"Score: {0}", font=FONT, align="center")

# Create and set up the turtle for displaying the countdown timer
turtle_time = turtle.Turtle()
turtle_time.hideturtle()
turtle_time.penup()
turtle_time.speed(0)
turtle_time.goto(0, turtle_screen.window_height()//2-75)

# Turtle object to display messages at the center of the screen
turtle_center = turtle.Turtle()
turtle_center.hideturtle()

# Variables for keeping track of the score and game time
score = 0
gametime = 20

# Function to move the turtle to a random location
def randomGoTurtle():
    turtle_instance.goto(randint(-turtle.window_width()//2, 0), randint(0, turtle.window_height()//2))
def countdown(time):
    turtle_time.clear()
    turtle_time.write(f"Time: {time}", font=FONT, align="center")
    # Move to a random location 2 times in 0.5 seconds
    for i in range(2):
        turtle.ontimer(randomGoTurtle(), 500)


# Function for increasing the score when the turtle is clicked
def increase_Score(x, y):
    global score
    score = score + 1
    show_score(score)

# Function to display the score on the screen
def show_score(score):
    turtle_score.clear()
    turtle_score.write(f"Score: {score}", font=FONT, align="center")

# Function for the countdown before starting the game
def countdownToStart(time):
    turtle_center.clear()
    turtle_center.write(time, font=("Arial", 36, "bold"), align="center")

# Countdown for 3, 2, 1, start
for i in range(3, -1, -1):
    turtle.ontimer(countdownToStart(i), 1000)
    turtle_center.clear()


# Countdown and turtle movement during the game time
for i in range(gametime, -1, -1):
    countdown(i)
    turtle_instance.onclick(increase_Score)


# Display the results when the game is over
turtle_center.write(f"Game Over\n Score: {score}", font=("Arial", 36, "bold"), align="center")

# Disable the click function for the turtle
turtle_instance.onclick(None)

# Close the turtle screen
turtle.done()