import turtle


# Function that draw the squares
def draw_squares(n):
    # First element
    first = 0
    # Second element
    second = 1

    # Setting the colour of the plotting pen to red
    drawer.pencolor("blue")

    # Drawing the initial square
    drawer.forward(second)
    drawer.left(90)
    drawer.forward(second)
    drawer.left(90)
    drawer.forward(second)
    drawer.left(90)
    drawer.forward(second)

    # Drawing the other ones
    for a in range(n - 1):
        # Fibonacci Series
        next_one = first + second
        first = second
        second = next_one

        drawer.backward(first)
        drawer.right(90)
        drawer.forward(second)
        drawer.left(90)
        drawer.forward(second)
        drawer.left(90)
        drawer.forward(second)


# Function that draw the spiral
def draw_spiral(n):
    # Bringing the pen to starting point of the spiral
    drawer.penup()
    drawer.setposition(1, 0)
    drawer.seth(0)
    drawer.pendown()

    # First element
    first = 0

    # Second element
    second = 1

    # Next element
    next_one = second

    # Setting the colour of the plotting pen to red
    drawer.pencolor("red")

    # Drawing the Spiral
    drawer.left(90)

    for i in range(n):
        print(next_one)
        spiral = 3.14 * next_one / 2
        spiral /= 90

        for j in range(90):
            drawer.forward(spiral)
            drawer.left(1)

        # Fibonacci Series
        second = first
        first = next_one
        next_one = first + second


# Receives the number of interactions the program will have
n_squares = int(input('Enter the number of squares (number> 0): '))

if n_squares > 0:
    drawer = turtle.Turtle()
    drawer.speed(100)
    draw_squares(n_squares)
    draw_spiral(n_squares)
    turtle.done()

else:
    print('Number of squares must be > 0')
