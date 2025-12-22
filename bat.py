import numpy as np
import matplotlib.pyplot as plt
import math

scale = 20

def batman_points():
    xs, ys = [], []

    # First curve
    for a in range(-7 * scale, -3 * scale, 1):
        x = a / scale
        rel = abs(x)
        y = 1.5 * math.sqrt((-abs(rel - 1)) * abs(3 - rel) / ((rel - 1) * (3 - rel))) * (
            1 + abs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
            4.5 + 0.75 * (abs(x - 0.5) + abs(x + 0.5)) - 2.75 * (
            abs(x - 0.75) + abs(x + 0.75))) * (1 + abs(1 - rel) / (1 - rel))
        xs.append(a)
        ys.append(y * scale)

    # Second curve
    for a in range(-3 * scale, -1 * scale - 1, 1):
        x = a / scale
        rel = abs(x)
        y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
            abs(rel - 1) / (rel - 1))
        xs.append(a)
        ys.append(y * scale)

    # Middle points
    xs += [-1 * scale, int(-0.5 * scale), int(0.5 * scale), 1 * scale]
    ys += [3 * scale, int(2.2 * scale), int(2.2 * scale), 3 * scale]

    # Symmetric right side
    for a in range(1 * scale + 1, 3 * scale + 1, 1):
        x = a / scale
        rel = abs(x)
        y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
            abs(rel - 1) / (rel - 1))
        xs.append(a)
        ys.append(y * scale)

    for a in range(3 * scale + 1, 7 * scale + 1, 1):
        x = a / scale
        rel = abs(x)
        y = 1.5 * math.sqrt((-abs(rel - 1)) * abs(3 - rel) / ((rel - 1) * (3 - rel))) * (
            1 + abs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
            4.5 + 0.75 * (abs(x - 0.5) + abs(x + 0.5)) - 2.75 * (
            abs(x - 0.75) + abs(x + 0.75))) * (1 + abs(1 - rel) / (1 - rel))
        xs.append(a)
        ys.append(y * scale)

    for a in range(7 * scale, 4 * scale, -1):
        x = a / scale
        rel = abs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(abs(rel - 4) / (rel - 4))
        xs.append(a)
        ys.append(y * scale)

    for a in range(4 * scale, -4 * scale, -1):
        x = a / scale
        rel = abs(x)
        y = abs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (abs(rel - 2) - 1) ** 2)
        xs.append(a)
        ys.append(y * scale)

    for a in range(-4 * scale - 1, -7 * scale - 1, -1):
        x = a / scale
        rel = abs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(abs(rel - 4) / (rel - 4))
        xs.append(a)
        ys.append(y * scale)

    return xs, ys

# Get points
xs, ys = batman_points()

# Plot with yellow background and black fill
fig, ax = plt.subplots(figsize=(8,5), facecolor="yellow")
ax.set_facecolor("yellow")

# Fill inside with black
ax.fill(xs, ys, color="black")

# Optional: outline glow effect
for i in range(6,0,-1):
    ax.plot(xs, ys, color="yellow", linewidth=i*2, alpha=0.08)  # glow layers
ax.plot(xs, ys, color="yellow", linewidth=2.5)  # sharp outline

ax.set_aspect("equal")
ax.axis("off")
plt.show()
       
