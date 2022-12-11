import turtle

def draw_triangle(x, y):
    pen.penup();

    #Points turtle to click
    pen.goto(x, y);

    pen.pendown();

    for _ in range(3):
        pen.forward(50);
        pen.left(120);

pen = turtle.Turtle();
turtle.onscreenclick(draw_triangle);
turtle.listen()
turtle.done();