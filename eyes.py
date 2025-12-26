import tkinter as tk
import math

# -----------------------
# Setup
# -----------------------
root = tk.Tk()
root.title("The Eyes Are Watching ")
WIDTH, HEIGHT = 800, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#0f0f14")
canvas.pack()

# Eye settings
eyes = [(300, 200), (500, 200)]
EYE_R = 50
PUPIL_R = 15
MAX_OFFSET = 20

# Draw eyes once
eye_items = []
pupil_items = []

for x, y in eyes:
    eye = canvas.create_oval(
        x - EYE_R, y - EYE_R,
        x + EYE_R, y + EYE_R,
        fill="white", outline=""
    )
    pupil = canvas.create_oval(
        x - PUPIL_R, y - PUPIL_R,
        x + PUPIL_R, y + PUPIL_R,
        fill="black"
    )
    
    eye_items.append(eye)
    pupil_items.append(pupil)

def follow_mouse(event):
    mx, my = event.x, event.y

    for i, (cx, cy) in enumerate(eyes):
        angle = math.atan2(my - cy, mx - cx)
        px = cx + math.cos(angle) * MAX_OFFSET
        py = cy + math.sin(angle) * MAX_OFFSET

        canvas.coords(
            pupil_items[i],
            px - PUPIL_R, py - PUPIL_R,
            px + PUPIL_R, py + PUPIL_R
        )

canvas.bind("<Motion>", follow_mouse)
root.mainloop()

