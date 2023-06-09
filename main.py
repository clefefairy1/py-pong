import turtle

#set up game screen
turtle.setup(800, 600)
turtle.bgcolor("black")
screen=turtle.Screen()

#set up ball
ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)

#set up paddles
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-300, 0)
paddle1.dy=0

paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(300,0)
paddle2.dy=0

#game rules
game_over = False 
winner = None
points = {
  "player1": 0,
  "player2": 0
}
game_rules = {
  "max_points": 3,
  "ball_speed": 3
}
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1 : 0  Player 2 : 0" , align = "center")

# Function to move paddle1 up
def paddle1_up():
    paddle1.dy = 10

# Function to move paddle1 down
def paddle1_down():
    paddle1.dy = -10

# Function to move paddle2 up
def paddle2_up():
    paddle2.dy = 10

# Function to move paddle2 down
def paddle2_down():
    paddle2.dy = -10


turtle.listen()

turtle.onkeypress(paddle1_up, "w")
turtle.onkeypress(paddle1_down, "s")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down, "Down")


screen.onkey
screen.listen()

#game rules
if points["player1"] == game_rules["max_points"]:
    game_over = True
    winner = "player1"
elif points["player2"] == game_rules["max_points"]:
    game_over = True
    winner = "player2"


# Ball movements
if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
    ball.setx(-340)
    ball.dx *= -1

# more ball movements
if ball.xcor() > 320:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player1"] += 1
elif ball.xcor() < -320:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player2"] += 1

if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

score_display.clear()
score_display.write("Player 1: {}  Player 2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))


# Game over screen
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write("Game Over! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))