import turtle
import random

# Creates n terms of the fibonacci function
def fibonacci_seq(n):
    sequence = [1,1];

    for i in range(n - 2):
        sequence.append(sequence[i] + sequence[i+1]);
        
    return sequence;

# Draw a square with a side length equals to length
def draw_square(length):

    for _ in range(4):
        pen.forward(length);
        pen.right(90);

# Make n squares
def make_squares(n, sequence):
    pen.pensize(3);

    for i in range(n):
        draw_square(scale * sequence[i]);
        pen.forward(scale * sequence[i]);
        pen.right(90);
        pen.forward(scale * sequence[i]);
        pen.pendown();

# Draw a spiral according to n
def draw_spiral(n, sequence):    
    pen.pensize(2);
    pen.penup();
    pen.pencolor("#F00");
    pen.setposition(0, 0);
    pen.setheading(0);
    pen.pendown();

    for i in range(n):
        pen.circle(-scale * sequence[i], 90);

# Plot the squares with the spiral
def make_spiral(n):
    fib_sequence = fibonacci_seq(n);
    pen.pencolor("#000");

    make_squares(n, fib_sequence);

    draw_spiral(n, fib_sequence);


while True:
    n = int(input("Enter the number of iterations. It must be > 1: "));
    if n > 1:
        break;

pen = turtle.Turtle();
scale = 10;
make_spiral(n);
turtle.done();