import turtle, random, math

# --- Setup ---
def setup_screen():
    screen = turtle.Screen()
    screen.setup(800, 500)
    screen.bgcolor(0.01, 0.01, 0.05)
    screen.tracer(0)
    return screen

def setup_pen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    return pen

# --- Stars ---
def create_stars(n=300):
    return [[random.randint(-400,400), random.randint(-250,250),
             random.randint(1,3), random.uniform(0.1,0.6),
             random.uniform(0.8,1.2), random.choice(["white","lightblue","yellow"])]
             for _ in range(n)]


def update_stars(stars, t, pen):
    for s in stars:
        s[1] -= s[3]
        if s[1] < -260:
            s[0], s[1] = random.randint(-400,400), 260
        size = int(s[2] * abs(math.sin(t * s[4])))
        pen.goto(s[0], s[1])
        pen.dot(max(1, size), s[5])

# --- Asteroid ---
def update_asteroid(ax, ay, t, trail, pen):
    ax += 7
    ay += math.sin(t) * 0.6
    trail.append((ax, ay))
    trail = trail[-30:]

    for i, p in enumerate(trail):
        pen.goto(p)
        pen.dot(max(1, i//2), (1, 0.5 + i/60, 0.2))

    pen.goto(ax, ay)
    pen.dot(10, "gray")
    pen.dot(14, (0.8, 0.8, 0.8))
    return ax, ay, trail

def reset_asteroid(ax, ay, trail, pen):
    for r in range(20, 80, 10):
        pen.goto(ax, ay)
        pen.dot(r, (1, random.random(), 0.3))
    return -450, random.randint(-120,120), []

# --- Shooting Star ---
def update_shooting_star(shooting, pen):
    if shooting:
        sx, sy = shooting
        pen.goto(sx, sy)
        pen.dot(5, "white")
        shooting[0] += 12
        shooting[1] -= 6
        if shooting[0] > 400 or shooting[1] < -250:
            shooting = None
    return shooting

# --- Main Loop ---
def main():
    screen = setup_screen()
    pen = setup_pen()
    stars = create_stars()

    ax, ay, t, trail, shooting = -450, random.randint(-120,120), 0, [], None

    while True:
        pen.clear()
        t += 0.05

        update_stars(stars, t, pen)
        ax, ay, trail = update_asteroid(ax, ay, t, trail, pen)

        if ax > 460:
            ax, ay, trail = reset_asteroid(ax, ay, trail, pen)

        if not shooting and random.random() < 0.002:
            shooting = [random.randint(-400,-200), 250]
        shooting = update_shooting_star(shooting, pen)

        screen.update()

# Run
main()

