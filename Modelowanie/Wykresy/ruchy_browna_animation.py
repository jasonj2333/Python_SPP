import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set random seed for reproducibility
np.random.seed(0)

num_particles = 30
box_size = 20
total_steps = 200

# Initialize particle positions and velocities
positionX = np.random.uniform(low=1, high=box_size-1, size=(num_particles, 1))
positionY = np.random.uniform(low=1, high=box_size-1, size=(num_particles, 1))

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)


# Initialize particles as scatter plot objects
particles = ax.scatter(positionX[:,0], positionY[:,0])

def update(frame, positionX,positionY):
    # Random displacements for particles
    displacementX =  np.random.normal(loc=0, scale=0.1, size=(num_particles, 1))
    displacementY =  np.random.normal(loc=0, scale=0.1, size=(num_particles, 1))

    # Update particle positions
    positionX += displacementX
    positionY += displacementY

    # Ensure particles stay within the box
    positionX = np.clip(positionX, 0, box_size)
    positionY = np.clip(positionY, 0, box_size)

    # Convert to Nx2 dimensions
    offsets = np.hstack((positionX, positionY))
    # Update scatter plot
    particles.set_offsets(offsets)

    return particles,

# Animation
ani = animation.FuncAnimation(fig, update, frames=total_steps, fargs=(positionX,positionY), interval=100, blit=True)

ani.save("brownian_mot.gif", writer="pillow")

plt.show()