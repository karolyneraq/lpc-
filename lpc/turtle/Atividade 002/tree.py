from turtle import *

speed('fastest')

# turning the turtle to face upwards
right(-90)

# the acute ANGLE between
# the base and branch of the Y
ANGLE = 30


# Draw lots of trunks (Y)
def draw_fractal_tree(size, level):

    if level > 0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255 // level, 0)

        # drawing the base
        forward(size)

        right(ANGLE)

        # recursive call for
        # the right subtree
        draw_fractal_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        left(2 * ANGLE)

        # recursive call for
        # the left subtree
        draw_fractal_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        right(ANGLE)
        forward(-size)


# tree of size 80 and level 7
draw_fractal_tree(80, 7)
