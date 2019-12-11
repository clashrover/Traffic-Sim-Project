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
	
	def loadNearJunc(self, posx, posy, velx, vely):
		junc = np.ones(2)
		junc = self.grid.searchNear(self.root,posx,posy,velx,vely)
		return junc