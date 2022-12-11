import turtle

def draw_tree(size, level):
    if level > 0:
        turtle.colormode(255);
        pen.pencolor(0, 255 // level, 0);

        #Draws the main branch
        pen.forward(size);

        pen.right(angle);

        #Draws the right sub-branch
        draw_tree(size * 0.8, level-1);

        pen.pencolor(0, 255 // level, 0);
        pen.left(2 * angle);

        #Draws the left sub-branch
        draw_tree(size * 0.8, level-1);

        pen.pencolor(0, 255 // level, 0);

        #Return the turtle to the start of the main branch
        pen.right(angle);
        pen.backward(size);


size = int(input("Enter the size of the main tree: "));
level = int(input("Enter the number of sub-trees: "));

# Define the angle between each branch of the tree
angle = 30;

pen = turtle.Turtle();

# Points the turtle upward
pen.left(90);

pen.speed('fastest');
draw_tree(size, level)

turtle.done();