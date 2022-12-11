import turtle

# Screen() method to get screen
turtle_screen = turtle.Screen()

# creating tess object
drawer = turtle.Turtle()


def draw_triangle(x, y):
    # it is used to draw out the pen
    drawer.penup()

    # it is used to move cursor at x
    # and y position
    drawer.goto(x, y)

    # it is used to draw in the pen
    drawer.pendown()

    for i in range(3):
        # move cursor 100 unit
        # digit forward
        drawer.forward(100)

        # turn cursor 120 degree left
        drawer.left(120)

        # Again,move cursor 100 unit
        # digit forward
        drawer.forward(100)


# special built-in function to send current
# position of cursor to triangle
turtle.onscreenclick(draw_triangle, 1)

turtle.listen()

# hold the screen
turtle.done()
