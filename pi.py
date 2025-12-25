# =========================
# Pi Day Art Project
# Create art using digits of pi in a spiral
# =========================

from turtle import *
import random
import math

# =========================
# SETUP
# =========================
hideturtle()
speed(5)
colormode(255)

# Random dark background
bgcolor(
    random.randint(0, 50),
    random.randint(0, 50),
    random.randint(0, 50)
)

# =========================
# PI DIGITS
# =========================
pi_string = "3.14159265358979323846264338327950287564747646465757"

# =========================
# STATE
# =========================
index = 0

# =========================
# DRAW FUNCTION
# =========================
def draw_digit():
    global index

    penup()

    # Spiral position (unchanged logic)
    x = index * 4 * math.sin(index)
    y = index * 4.2 * math.cos(index)
    goto(x, y)

    # Random bright color
    color(
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255)
    )

    # Random font size
    style = ('Courier', random.randint(20, 25), 'bold')

    pendown()
    write(pi_string[index], move=True, font=style, align='center')

    index += 1

# =========================
# MAIN LOOP
# =========================
while True:
    draw_digit()

