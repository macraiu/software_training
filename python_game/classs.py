import turtle
import numpy as np


class game(turtle.Turtle):

    backgnd_color = "black"
    default_obj_color = "white"
    default_obj_shape = "square"

    @classmethod
    def init_screen(cls):
        wn = turtle.Screen()
        wn.title("Pong by Craiu")
        wn.bgcolor("black")
        wn.setup(width=800, height=600)
        wn.tracer(0)

        print("Initialised")
        #keyboard binding
        wn.listen()

        return wn

    @classmethod
    def create_game_object(cls, speed = 0, size_stretch=[1, 1], pose = [0, 0],
                            shape = default_obj_shape, color = default_obj_color):
        game_object = turtle.Turtle()
        game_object.speed(0)
        game_object.shape(shape)
        game_object.shapesize(stretch_wid=size_stretch[0], stretch_len=size_stretch[1])
        game_object.goto(pose[0], pose[1])
        game_object.color(color)
        game_object.penup()
        return game_object

    
#function 
def paddle_a_up():
    y = paddle_a.ycor()
    #returns y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    #returns y coordinate
    y -= 20
    paddle_a.sety(y)

#function 
def paddle_b_up():
    y = paddle_b.ycor()
    #returns y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    #returns y coordinate
    y -= 20
    paddle_b.sety(y)

wn = game.init_screen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

paddle_a = game.create_game_object(size_stretch = [5, 1], pose = [-350, 0])
paddle_b = game.create_game_object(size_stretch = [5, 1], pose = [350, 0])
ball = game.create_game_object()



#divide the ball direction in x and y
ball.dx = 0.1
ball.dy = 0.1
#every time the ball moves will move by 2 pixels









#needs main game loop 
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if abs(ball.ycor()) > 290:
        ball.sety(np.sign(ball.ycor()) * 290)
        ball.dy *= -1
    
    #if abs(ball.xcor()) > 390:
    #    ball.setx(np.sign(ball.xcor()) * 390)
    #    ball.dx *= -1

    if abs(ball.xcor()) > 390:
        ball.goto(0, 0)
        ball.dx *= -1