import numpy as np
import matplotlib.pyplot as plt

# --- Shared function and grid ---
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)
z = f(x, y)

# --- First visualization: contour3D ---
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
ax1.contour3D(x, y, z, 50, cmap='binary')
ax1.set_title('3D Contour')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
plt.show()

# --- Second visualization: wireframe ---
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_wireframe(x, y, z, color='black')
ax2.set_title('Wireframe')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
plt.show()

# --- Third visualization: surface plot ---
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot_surface(x, y, z, rstride=1, cstride=1,
                 cmap='viridis', edgecolor='none')
ax3.set_title('Surface')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
plt.show()
 
       

 
       

