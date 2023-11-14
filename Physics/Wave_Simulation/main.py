# Program for finding the position of Neptune from Uranus's
# orbit anomalies

import matplotlib
matplotlib.use("TkAgg")
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


from RungeKuttaStuff import RungeKutta


# User Chosen Parameters
number_of_springs = 100
time_step_size = 0.01
damping_coefficient = 0.0
spring_constant = 100
mass = 1
resting_length = 0

# Plot parameters
total_time = 50

# Initializing Needed Vectors, with an initial condition
y_position = np.zeros(number_of_springs)
y_velocity = np.zeros(number_of_springs)
x = np.linspace(0, total_time, number_of_springs)

# I.C. here
#y_position[1] = 1
#y_velocity[5] = 1

for spring in range(1, number_of_springs-1, 1):
    y_position[spring] = math.sin(x[spring])
    y_velocity[spring] = - math.sqrt(spring_constant / mass) * math.cos(x[spring])

rk = RungeKutta(y_position, y_velocity, time_step_size,
                damping_coefficient, spring_constant, mass, number_of_springs,
                resting_length)


# Main loop area
t = 0
dt = 1
t_end = 10
spring_two = []


# Create a figure and axis
fig, ax = plt.subplots()
points, = ax.plot(x[:], y_position[:], 'o')

# Set plot limits
ax.set_xlim(0, total_time)
ax.set_ylim(-3, 3)


def update(frame):
    print(frame)
    for spring in range(1, number_of_springs-1, 1):
        y_position[spring], y_velocity[spring] = rk.main(spring)


    # Update the plot with new positions
    points.set_data(x[1:number_of_springs - 1], y_position[1:number_of_springs-1])

    return points,


ani = FuncAnimation(fig, update, frames=1000, interval=100,
                    blit=False, repeat=False)
plt.show()
