import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import math
import Map
import time

class subLight():
	def __init__(self, direction):
		self.red = False
		self.green = True
		self.direction = direction

	def setGreen(self,):
		self.red = False
		self.green = True

	def setRed(self,):
		self.red = True
		self.green = False


class light():
	lights =[]
	def __init__(self,):
		self.lights.append(subLight(1))
		self.lights.append(subLight(2))
		self.lights.append(subLight(3))
		self.lights.append(subLight(4))
		self.setGreen(2)

	def setGreen(self, direction):
		x = direction-1
		for i in range(3):
			self.lights[i].setRed()
		
		self.lights[x].setGreen()

	def checkRed(self,direction):
		return self.lights[direction-1].red



	


	