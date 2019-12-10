import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import math
import vehicle
import AVLTree as tree

class Junction():
	pos_x=0
	pos_y=0
	def __init__(self, posx, posy):
		self.pos_x = posx
		self.pos_y = posy
		plt.plot([posx-0.5, posx-0.1], [posy-0.05, posy-0.05], color='k', linestyle='-', linewidth=1)
		plt.plot([posx-0.5, posx-0.1], [posy+0.05, posy+0.05], color='k', linestyle='-', linewidth=1)
		plt.plot([posx+0.1, posx+0.5], [posy-0.05, posy-0.05], color='k', linestyle='-', linewidth=1)
		plt.plot([posx+0.1, posx+0.5], [posy+0.05, posy+0.05], color='k', linestyle='-', linewidth=1)
		plt.plot([posx-0.05, posx-0.05], [posy-0.5, posy-0.1], color='k', linestyle='-', linewidth=1)
		plt.plot([posx+0.05, posx+0.05], [posy-0.5, posy-0.1], color='k', linestyle='-', linewidth=1)
		plt.plot([posx-0.05, posx-0.05], [posy+0.1, posy+0.5], color='k', linestyle='-', linewidth=1)
		plt.plot([posx+0.05, posx+0.05], [posy+0.1, posy+0.5], color='k', linestyle='-', linewidth=1)
		plt.plot([posx-0.1, posx-0.05], [posy+0.05, posy+0.1], color='k', linestyle='-', linewidth=1)
		plt.plot([posx-0.1, posx-0.05], [posy-0.05, posy-0.1], color='k', linestyle='-', linewidth=1)
		plt.plot([posx+0.05, posx+0.1], [posy+0.1, posy+0.05], color='k', linestyle='-', linewidth=1)
		plt.plot([posx+0.05, posx+0.1], [posy-0.1, posy-0.05], color='k', linestyle='-', linewidth=1)
		plt.plot([posx-0.5,posx+0.5], [posy, posy], color='k', linestyle='--', linewidth=1)
		plt.plot([posx, posx], [posy-0.5, posy+0.5], color='k', linestyle='--', linewidth=1)
		


class Grid():
	grid = tree.AVLTree()
	root = None
	def addJunction(self, junc):
		self.root = self.grid.insert(self.root, junc.pos_x, junc.pos_y)
	


n = 3               # Number of cars
m = np.ones(n)      # car massess
x = np.zeros((n,2)) # Particle positions (x and y for ith particle in x[i,0], x[i,1])
cars = []   #list of cars
# initialize all the cars
cars.append(vehicle.car(0, 0.525, 5, 0,cars))
cars.append(vehicle.car(1, 0.475, -5, 0,cars))
cars.append(vehicle.car(0.475, 0, 0, 5,cars))
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

# Drawing code
fig, ax = plt.subplots()
points, = ax.plot(x[:,0], x[:,1], 'o')
grid = Grid()
grid.addJunction(Junction(0.5,0.5))
grid.addJunction(Junction(1.5,0.5))
grid.addJunction(Junction(0.5,1.5))
grid.addJunction(Junction(1.5,1.5))

def init():
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
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
