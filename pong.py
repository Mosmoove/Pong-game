import turtle 
#importing turtle to build the graphics
#Creating the window screen
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("white")
window.setup(width = 800, height = 600)
window.tracer(0) # speeds up the game

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # sets the speed to maximum possible speed
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0) # starting position of paddle a

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.xspeed = 3 # every time the ball moves by 2px
ball.yspeed = 3

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align = "center", font =("courier", 24, "normal"))

#Scores
score_1 = 0 #paddle A represents score 1
score_2 = 0 # paddle B represents score 2

def paddle_a_move_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_move_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_move_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_move_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# Keyboard binding
def eventListen():
    window.listen() #listens for an action/event
    window.onkeypress(paddle_a_move_up, "w")
    window.onkeypress(paddle_a_move_down, "s")
    window.onkeypress(paddle_b_move_up, "Up")
    window.onkeypress(paddle_b_move_down, "Down")

eventListen()

#Main
while True:
    window.update()
    
    ball.setx(ball.xcor() + ball.xspeed)
    ball.sety(ball.ycor() + ball.yspeed)
    
    #Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.yspeed *= -1 # reverses the direction
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yspeed *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.xspeed *= -1
        score_1 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1}  Player 2: {score_2}", align = "center", font =("courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.xspeed *= -1
        score_2 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1}  Player 2: {score_2}", align = "center", font =("courier", 24, "normal"))
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.xspeed *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.xspeed *= -1


    
    

