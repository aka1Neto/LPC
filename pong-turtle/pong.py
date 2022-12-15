import os
import turtle

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Draws a paddle
def draw_paddle(position):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(position, 0)

    return paddle


paddle_1 = draw_paddle(-350)
paddle_2 = draw_paddle(350)


# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_up(paddle):
    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle.sety(y)


# keyboard
screen.listen()
screen.onkeypress(lambda: paddle_up(paddle_1), "w")
screen.onkeypress(lambda: paddle_down(paddle_1), "s")
screen.onkeypress(lambda: paddle_up(paddle_2), "Up")
screen.onkeypress(lambda: paddle_down(paddle_2), "Down")

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        os.system("afplay bounce.wav&")
        ball.sety(-290)
        ball.dy *= -1

    def update_score(score):
        score += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1

        return score


    # collision with left wall
    if ball.xcor() < -390:
        score_2 = update_score(score_2)

    # collision with right wall
    if ball.xcor() > 390:
        score_1 = update_score(score_1)

    # collision with the paddle 1
    if -330 > ball.xcor() > -350 \
            and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # collision with the paddle 2
    if 330 < ball.xcor() < 350 \
            and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
