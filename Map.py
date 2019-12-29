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
	cars = None
	maxClearance = 0.2
	minClearance = 0.05
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
		cars = []

	def checkSignal(self,direction):
		# return self.light.checkRed(direction)
		return False

	def addCar(self,car):
		cars.append(car)

	def removeCar(self,car):
		cars.remove(car)

	def searchNearestCar(self,car):
		for obj in cars:
			if obj.vel_x>0.1 and car.vel_x>0.1:
				if obj.pos_x>car.pos_x :
					d = obj.pos_x-car.pos_x
					if d<self.maxClearance and d>self.minClearance:
						return obj

			if obj.vel_x<-0.1 and car.vel_x<-0.1:
				if obj.pos_x<car.pos_x :
					d = car.pos_x-obj.pos_x
					if d<self.maxClearance and d>self.minClearance:
						return obj

			if obj.vel_y>0.1 and car.vel_y>0.1:
				if obj.pos_y>car.pos_y :
					d = obj.pos_y-car.pos_y
					if d<self.maxClearance and d>self.minClearance:
						return obj

			if obj.vel_y<-0.1 and car.vel_y<-0.1:
				if obj.pos_y<car.pos_y :
					d = car.pos_y-obj.pos_y
					if d<self.maxClearance and d>self.minClearance:
						return obj


class Grid():
	grid = tree.AVLTree()
	root = None

	def addJunction(self, junc):
		self.root = self.grid.insert(self.root, junc.center_x, junc.center_y, junc)
	
	def loadNearJunc(self, posx, posy, velx, vely):
		junc = self.grid.searchNear(self.root,posx,posy,velx,vely)
		return junc
