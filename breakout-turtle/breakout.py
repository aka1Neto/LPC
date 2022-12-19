import turtle

# draw screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=700, height=800)
screen.tracer(0)


# Function that draw a paddle
def draw():
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.penup()

    return paddle


# draw and set paddle 1
player = draw()
player.shapesize(stretch_wid=0.5, stretch_len=3)
player.goto(0, -350)

# draw bricks
colors = ["red", "red", "orange", "orange", "green", "green", "yellow", "yellow"]
bricks = []

for i in range(8):

    for j in range(14):
        brick = draw()
        brick.color(colors[i])
        brick.shapesize(stretch_wid=0.5, stretch_len=2)
        brick.goto(-312 + (j*48), 260 - (i*15))
        bricks.append(brick)

# draw ball
ball = draw()
ball.shapesize(stretch_wid=0.25, stretch_len=0.25)
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# counters and verifiers
score = 0
lives = 1
collide = 1

# head-up display
hud_lives = draw()
hud_lives.hideturtle()
hud_lives.goto(-250, 300)
hud_lives.write("lives: 1", align="center", font=("Press Start 2P", 24, "normal"))

hud_score = draw()
hud_score.hideturtle()
hud_score.goto(-150, 270)
hud_score.write("Score: 0", align="center", font=("Press Start 2P", 24, "normal"))

hud_game_over = draw()
hud_game_over.hideturtle()
hud_game_over.goto(0, 20)

# draw walls
upper_wall = draw()
upper_wall.shapesize(stretch_wid=2, stretch_len=34)
upper_wall.penup()
upper_wall.goto(0, 370)

right_wall = draw()
right_wall.shapesize(stretch_wid=39, stretch_len=0.25)
right_wall.penup()
right_wall.goto(340, 0)

left_wall = draw()
left_wall.shapesize(stretch_wid=39, stretch_len=0.25)
left_wall.penup()
left_wall.goto(-340, 0)


def paddle_right():

    coord_x = player.xcor()

    if coord_x < 310:

        coord_x += 31

    else:

        coord_x = 310

    player.setx(coord_x)


def paddle_left():

    coord_x = player.xcor()

    if coord_x > -310:

        coord_x += -31

    else:

        coord_x = -310

    player.setx(coord_x)


# keyboard
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")


# Collision with a brick
def collide_brick(ball_in_game, target_brick):

    if target_brick.ycor() - 8 <= ball_in_game.ycor() <= target_brick.ycor() + 8 and \
            target_brick.xcor() - 23 <= ball_in_game.xcor() <= target_brick.xcor() + 23 and \
            collide == 1:

        ball_in_game.dy *= -1
        ball_in_game.sety(target_brick.ycor()+(ball_in_game.dy*8))
        target_brick.hideturtle()

        return 1

    else:

        return 0


while True:

    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if lives > 4:

        break

    # collision with the upper wall
    if ball.ycor() > 350:

        ball.sety(350)
        ball.dy *= -1

        if collide == 0:

            collide = 1

    # collision with lower wall
    if ball.ycor() < -370:

        lives += 1
        hud_lives.clear()
        hud_lives.write("lives: {}".format(lives), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

        if collide == 0:

            collide = 1

    # collision with left wall
    if ball.xcor() < -335:

        ball.setx(-335)
        ball.dx *= -1

        if collide == 0:

            collide = 1

    # collision with right wall
    if ball.xcor() > 335:

        ball.setx(335)
        ball.dx *= -1

        if collide == 0:

            collide = 1

    # collision with the right side of the paddle with the ball coming from
    # the right side
    if ball.ycor() < -340 and player.xcor() < ball.xcor() < player.xcor() + 30 and ball.dx == -1:

        ball.sety(-340)
        ball.dy *= -1
        ball.dx *= -1

        if collide == 0:

            collide = 1

    # collision with the right side of the paddle with the ball coming from
    # the left side
    elif ball.ycor() < -340 and player.xcor() <= ball.xcor() <= player.xcor() + 30 and ball.dx == 1:

        ball.sety(-340)
        ball.dy *= -1

        if collide == 0:

            collide = 1

    # collision with the left side of the paddle with the ball coming from
    # the left side
    elif ball.ycor() < -340 and player.xcor() - 30 < ball.xcor() < player.xcor() and ball.dx == 1:

        ball.sety(-340)
        ball.dy *= -1
        ball.dx *= -1

        if collide == 0:

            collide = 1

    # collision with the left side of the paddle with the ball coming from
    # the right side
    elif ball.ycor() < -340 and player.xcor() - 30 <= ball.xcor() <= player.xcor() and ball.dx == -1:

        ball.sety(-340)
        ball.dy *= -1

        if collide == 0:

            collide = 1

    for i in range(len(bricks)):

        if collide_brick(ball, bricks[i]) == 1:

            if bricks[i].color()[0] == "red":

                score += 7

            elif bricks[i].color()[0] == "orange":

                score += 5

            elif bricks[i].color()[0] == "green":

                score += 3

            elif bricks[i].color()[0] == "yellow":

                score += 1

            hud_score.clear()
            hud_score.write("Score: {}".format(score), align="center", font=("Press Start 2P", 24, "normal"))

            collide = 0

            del(bricks[i])

            break

hud_game_over.write("Game Over", align="center", font=("Press Start 2P", 24, "normal"))

turtle.done()
