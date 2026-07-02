import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")       # Sets the background color to black
screen.title("Animated Rainbow Mesh Spiral")

# Turtle (pen) setup
t = turtle.Turtle()
t.speed(0)                    # Sets the animation speed to the fastest
t.width(2)                    # Sets the thickness of the lines

# Number of iterations (increase for a larger and more complex mesh)
iterations = 400

# Animation loop
for i in range(iterations):
    # Generating rainbow colors using HSV to RGB conversion
    color = colorsys.hsv_to_rgb(i / iterations, 1.0, 1.0)
    t.pencolor(color)
    
    # Core logic to create the geometric mesh pattern
    t.forward(i * 1.2)        # Moves forward, increasing distance slightly each time
    t.left(145)               # Turns at a specific angle
    t.forward(i * 0.5)
    t.left(45)

    # Setup to write the signature text smoothly
t.penup()
t.goto(150, -320)             # Positions the text at the bottom right corner
t.pencolor("white")           # Clean white text color
t.write("DEVELOPED BY - MD.FAHAD HOSSAIN", align="right", font=("Arial", 12, "bold"))
t.hideturtle()                # Hides the turtle drawing cursor

# Keeps the window open after the drawing is complete
turtle.done()