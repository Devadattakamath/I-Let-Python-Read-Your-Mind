import tkinter as tk

root = tk.Tk()
root.title("YouTube Popup")
root.geometry("500x300")
root.overrideredirect(True)

# Center window
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w // 2) - (500 // 2)
y = (screen_h // 2) - (300 // 2)
root.geometry(f"500x300+{x}+{y}")

# Canvas for gradient background
canvas = tk.Canvas(root, width=500, height=300, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def draw_gradient():
    for i in range(300):
        r = int(30 + (120-30) * (i/300))
        g = int(30 + (60-30) * (i/300))
        b = int(80 + (200-80) * (i/300))
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, 500, i, fill=color)

draw_gradient()

# Title text (typewriter loop)
title_label = canvas.create_text(250, 80, text="", font=("Arial", 28, "bold"), fill="white")
text_to_type = "Watch till end"
typed_text = ""
index = 0
direction = 1  # 1 = typing, -1 = erasing

def typewriter():
    global typed_text, index, direction
    if direction == 1:  # typing
        if index < len(text_to_type):
            typed_text += text_to_type[index]
            index += 1
        else:
            direction = -1
    else:  # erasing
        if index > 0:
            typed_text = typed_text[:-1]
            index -= 1
        else:
            direction = 1
    canvas.itemconfig(title_label, text=typed_text)
    root.after(150, typewriter)

# Messages cycling
messages = ["Like 👍", "Comment 💬", "Subscribe 🔔"]
msg_index = 0
msg_label = canvas.create_text(250, 140, text=messages[0], font=("Arial", 22, "bold"), fill="yellow")

def cycle_messages():
    global msg_index
    msg_index = (msg_index + 1) % len(messages)
    canvas.itemconfig(msg_label, text=messages[msg_index])
    root.after(2000, cycle_messages)

# Rounded Subscribe button with shadow
button_rect = None
button_text = None

def draw_button():
    global button_rect, button_text
    x0, y0, x1, y1 = 150, 200, 350, 260
    # shadow
    canvas.create_oval(x0+5, y0+5, x1+5, y1+5, fill="black", outline="")
    # rounded pill
    button_rect = canvas.create_oval(x0, y0, x1, y1, fill="red", outline="")
    button_text = canvas.create_text(250, 230, text="SUBSCRIBE 🔔", font=("Arial", 20, "bold"), fill="white")

draw_button()

# Heartbeat pulse for button
scale = 1.0
pulse_dir = 1

def pulse():
    global scale, pulse_dir
    scale += 0.02 * pulse_dir
    if scale > 1.2:
        pulse_dir = -1
    elif scale < 0.9:
        pulse_dir = 1
    size = int(20 * scale)
    canvas.itemconfig(button_text, font=("Arial", size, "bold"))
    root.after(50, pulse)

# Auto-close with fade
fade_alpha = 1.0
def fade_out():
    global fade_alpha
    fade_alpha -= 0.05
    if fade_alpha <= 0:
        root.destroy()
    else:
        root.attributes("-alpha", fade_alpha)
        root.after(100, fade_out)

# Start animations
typewriter()
cycle_messages()
pulse()
root.after(12000, fade_out)  # close after 12s

root.mainloop()
