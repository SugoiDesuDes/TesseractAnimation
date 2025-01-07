import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of a 4D cube (tesseract)
vertices = np.array([
    [-1, -1, -1, -1],
    [ 1, -1, -1, -1],
    [ 1,  1, -1, -1],
    [-1,  1, -1, -1],
    [-1, -1,  1, -1],
    [ 1, -1,  1, -1],
    [ 1,  1,  1, -1],
    [-1,  1,  1, -1],
    [-1, -1, -1,  1],
    [ 1, -1, -1,  1],
    [ 1,  1, -1,  1],
    [-1,  1, -1,  1],
    [-1, -1,  1,  1],
    [ 1, -1,  1,  1],
    [ 1,  1,  1,  1],
    [-1,  1,  1,  1]
])

# Define the edges of the 4D cube
edges = np.array([
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7],
    [8, 9], [9, 10], [10, 11], [11, 8],
    [12, 13], [13, 14], [14, 15], [15, 12],
    [8, 12], [9, 13], [10, 14], [11, 15],
    [0, 8], [1, 9], [2, 10], [3, 11],
    [4, 12], [5, 13], [6, 14], [7, 15]
])

# Function to project 4D space onto 3D space
def project_4d_to_3d(vertices, ana, kata):
    return np.array([v[:3] * (ana - v[3]) / (kata - v[3]) for v in vertices])

# Initialize the plot
def init():
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

# Update the plot
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ana = np.cos(frame / 30.0)
    kata = np.sin(frame / 30.0)
    projected_vertices = project_4d_to_3d(vertices, ana, kata)
    for edge in edges:
        ax.plot(projected_vertices[edge, 0], projected_vertices[edge, 1], projected_vertices[edge, 2], c='b')

ani = animation.FuncAnimation(fig, update, frames=360, interval=50)
plt.show()