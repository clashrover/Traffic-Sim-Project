import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import math
import vehicle
import AVLTree as tree
import light

class Junction():
	center_x=0
	center_y=0
	light = None
	def __init__(self, posx, posy):
		self.center_x = posx
		self.center_y = posy
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
		self.light = light.light()

	def checkSignal(self,direction):
		# return self.light.checkRed(direction)
		return False



class Grid():
	grid = tree.AVLTree()
	root = None

	def addJunction(self, junc):
		self.root = self.grid.insert(self.root, junc.center_x, junc.center_y, junc)
	
	def loadNearJunc(self, posx, posy, velx, vely):
		junc = self.grid.searchNear(self.root,posx,posy,velx,vely)
		return junc
