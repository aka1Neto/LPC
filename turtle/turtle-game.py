from random import choice
import turtle

# Defines the finish line for each turtle
def define_home():

    player1.shape('turtle');
    player1.color('#F00');
    player1.penup();
    player1.goto(200, 60);
    player1.pendown();
    player1.circle(40);

    player2.shape('turtle');
    player2.color('#00F');
    player2.penup();
    player2.goto(200, -140);
    player2.pendown();
    player2.circle(40);    
    

# Put the turtles at the startin line
def position_turtle():

    player1.penup();
    player1.goto(-200, 100);

    player2.penup();
    player2.goto(-200, -100);


# Plays the game itself
def game():
    dice = [1, 2, 3, 4, 5, 6];

    while True:

        if player1.position() >= (200, 100):
            print("Player 1 won!!");
            break;

        elif player2.position() >= (200, -100):
            print("Player 2 won!!");
            break;

        else:
            input("Player 1 turn. Press 'Enter' to roll the dice.");
            steps_number = (choice(dice) * 20);
            print(f"The number of steps will be: {steps_number}.");
            player1.forward(steps_number);

            if player1.position() >= (240, 100):
                player1.goto(240, 100);

            input("Player 2 turn. Press 'Enter' to roll the dice.");
            steps_number = (choice(dice) * 20);
            print(f"The number of steps will be: {steps_number}.");
            player2.forward(steps_number);

            if player2.position() >= (240, -100):
                player2.goto(240, -100);


player1 = turtle.Turtle();
player2 = turtle.Turtle();
define_home();
position_turtle();
game();

turtle.done();