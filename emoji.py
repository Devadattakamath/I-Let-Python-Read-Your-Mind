import tkinter as tk
import random

# Emoji pool
emojis = ["😀", "✨", "🔥", "🚀", "💻", "🎉", "🐍"]

# Color pool
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta", "white"]

# Create popup window
root = tk.Tk()
root.title("Colorful Emoji Rain")
root.geometry("400x600")
canvas = tk.Canvas(root, bg="black")
canvas.pack(fill="both", expand=True)

def create_emoji():
    emoji = random.choice(emojis)
    color = random.choice(colors)
    x = random.randint(20, 380)
    text = canvas.create_text(x, 0, text=emoji, font=("Arial", 20), fill=color)
    fall(text)

def fall(text):
    def animate():
        coords = canvas.coords(text)
        if coords and coords[1] < 580:  # still inside window
            canvas.move(text, 0, 5)     # move down
            root.after(50, animate)     # repeat
        else:
            canvas.delete(text)         # disappear at bottom
    animate()

def rain():
    create_emoji()
    root.after(300, rain)  # spawn new emoji every 300ms

rain()
root.mainloop()

