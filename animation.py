import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import math
import vehicle
import AVLTree as tree
import Map 



n = 6               # Number of cars
m = np.ones(n)      # car massess
x = np.zeros((n,2)) # Particle positions (x and y for ith particle in x[i,0], x[i,1])

# Drawing code
fig, ax = plt.subplots()
points, = ax.plot(x[:,0], x[:,1], 'o')
grid = Map.Grid()
grid.addJunction(Map.Junction(0.5,0.5))
grid.addJunction(Map.Junction(0.5,1.5))
grid.addJunction(Map.Junction(0.5,2.5))
grid.addJunction(Map.Junction(1.5,0.5))
grid.addJunction(Map.Junction(1.5,1.5))
grid.addJunction(Map.Junction(1.5,2.5))
grid.addJunction(Map.Junction(2.5,0.5))
grid.addJunction(Map.Junction(2.5,1.5))
grid.addJunction(Map.Junction(2.5,2.5))


cars = []   #list of cars
# initialize all the cars
#cars.append(vehicle.car(1.25, 0.525, 5, 0,cars,grid))
cars.append(vehicle.car(1, 0.525, 4.2, 0,cars,grid))
cars.append(vehicle.car(1.1, 1.525, 4.2, 0,cars,grid))
cars.append(vehicle.car(2.1, 2.475, -4.2, 0,cars,grid))
cars.append(vehicle.car(2.1, 0.475, -4.2, 0,cars,grid))
cars.append(vehicle.car(0.475, 1, 0, 4.3,cars,grid))
cars.append(vehicle.car(0.525, 1, 0, -4.3,cars,grid))
# cars.append(vehicle.car(1, 0.475, -3.9, 0,cars,grid))
# cars.append(vehicle.car(2, 0.475, -3.9, 0,cars,grid))
# cars.append(vehicle.car(0.475, 2, 0, 3.9,cars,grid))
#cars[0].setSeq(2)
cars[0].setDestination(0,0.475)
cars[1].setDestination(0,1.475)
cars[2].setDestination(3,2.525)
cars[3].setDestination(3,0.525)
cars[4].setDestination(0.525,0)
cars[5].setDestination(0.475,3)

# cars[5].setDestination(0,1,2,0,1,0)
# cars[6].setDestination(2,1,1,2,0,0)
# cars[7].setDestination(2,1,1,2,0,1)
#cars.append(vehicle.car(1, 0.475, -5, 0,cars,grid))
# cars.append(vehicle.car(0.475, 0, 0, 5,cars,grid))
# list[0].setList(list)
# list[1].setList(list)

dt = 0.001           # Time step


x[0,:] = np.array([0,0])

# Time stepping (this is actually "semi-implicit Euler")
def step():
    # Accumulate forces on each particle
    i=0
    for obj in cars:
    	obj.update()
    
    for i in range(n):
    	x[i,0]=cars[i].pos_x
    	x[i,1]=cars[i].pos_y




# for obj in cars:
# 	obj.setGrid(grid)

def init():
    ax.set_xlim(0,3)
    ax.set_ylim(0,3)
    ax.set_aspect('equal')
    return points,

def animate(frame):
    step()
    points.set_data(x[:,0], x[:,1])
    if frame is frames-1:
        plt.close()
    return points,

totalTime = 1
frames = int(totalTime/dt)
anim = FuncAnimation(fig, animate, frames=range(frames), init_func=init, interval=dt*1000)
plt.show()
