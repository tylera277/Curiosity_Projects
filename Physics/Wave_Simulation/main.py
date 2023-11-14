# Program for finding the position of Neptune from Uranus's
# orbit anomalies

import numpy as np
import matplotlib;
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from RungeKuttaStuff import RungeKutta


# User Chosen Parameters
number_of_springs = 10
time_step_size = 0.01
damping_coefficient = 0
spring_constant = 80
mass = 10

# Initializing Needed Vectors, with an initial condition
y_position = np.zeros(number_of_springs)
y_velocity = np.zeros(number_of_springs)

# I.C. here
#y_position[5] = 1
#y_velocity[5] = 1

#for spring in range(1, number_of_springs-1, 1):
#    y_position[spring] = ( y_position[spring-1] - y_position[spring+1] ) / 2.0


rk = RungeKutta(y_position, y_velocity, time_step_size,
                damping_coefficient, spring_constant, mass, number_of_springs)


# Main loop area
t = 0
dt = 1
t_end = 10
spring_two = []

x = np.linspace(0, 1, number_of_springs)

# Create a figure and axis
fig, ax = plt.subplots()
points, = ax.plot(x[:], y_position[:], 'o')

# Set plot limits
ax.set_xlim(0, 1)
ax.set_ylim(-2, 2)


def update(frame):
    print(frame)
    for spring in range(1, number_of_springs-1, 1):
        y_position, y_velocity = rk.main(spring)


    # Update the plot with new positions
    points.set_data(x[:], y_position[:])

    return points,

ani = FuncAnimation(fig, update, frames=100, interval=100, blit=False)
plt.show()
