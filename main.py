import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(height=800, width=1400)
screen.bgcolor('grey')
is_race = False
user_choice = screen.textinput(title="Make your bet",
                               prompt="Which turtle will win the race? Enter a color: ")
list_of_objects_color = ["red", "orange", "black", "yellow", "blue", "purple"]
x_width = [-350, -250, -150, 0, 150, 250]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(0)
    new_turtle.shapesize(2)
    new_turtle.color(list_of_objects_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-650, y=x_width[turtle_index])
    all_turtles.append(new_turtle)
if user_choice:
    is_race = True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 650:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You have won! {winning_color} is the winner")
            else:
                print(f"You have lost! {winning_color} is the winner")
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        turtle.speed(0)

screen.exitonclick()
