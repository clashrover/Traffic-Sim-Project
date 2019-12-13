import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import math
import Map

class car():
	dt = 0.001
	pos_x = 0
	pos_y = 0
	vel_x = 0
	vel_y = 0
	di = 0
	dt=0.001
	seq = []
	cars = []
	grid = None
	currentJunc = None
	avgVel =0
	def __init__(self, pos_x, pos_y, vel_x, vel_y,cars,grid):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.seq.append(2)
		self.di = 0
		self.cars = cars
		self.grid = grid
		self.currentJunc = self.grid.loadNearJunc(pos_x,pos_y,vel_x,vel_y)
		self.avgVel = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))

	def reset(self,):
		self.vel_x=0
		self.vel_y=0



	def update(self, ):
		if(self.checkInter()):
			self.takeTurn()
		else:
			self.maintSide()
			self.currentJunc = self.grid.loadNearJunc(self.pos_x,self.pos_y,self.vel_x,self.vel_y)
			#self.checkBoundary()

	def checkInter(self, ):
		X = self.currentJunc[0]
		Y = self.currentJunc[1]
		return bool(self.pos_y<Y+0.2 and self.pos_y>Y-0.2 and self.pos_x<X+0.2 and self.pos_x>X-0.2)

	def getState(self, ):
		X=self.currentJunc[0]
		Y=self.currentJunc[1]
		if(self.pos_x<X-0.15 and self.pos_x>X-0.16 and abs(self.vel_y)<0.2 and self.vel_x>0.2):
			self.di = 1
		elif(self.pos_x>X+0.15 and self.pos_x<X+0.16 and abs(self.vel_y)<0.2 and self.vel_x<-0.2):
			self.di = 2
		elif(self.pos_y<Y-0.15 and self.pos_y>Y-0.16 and abs(self.vel_x)<0.2 and self.vel_y>0.2):
			self.di = 3
		elif(self.pos_y>Y+0.15 and self.pos_y<Y+0.16 and abs(self.vel_x)<0.2 and self.vel_y<-0.2):
			self.di = 4
		
	def takeTurn(self, ):
		c = self.seq[0]
		f = np.ones(2)
		self.getState()
		X=self.currentJunc[0]
		Y=self.currentJunc[1]
		if(c==0):
			if(self.di==1):
				if(self.pos_x>X-0.15 and self.pos_x<X-0.11 and self.pos_y<Y+0.05 and self.pos_y>Y):
					#exponential decay
					if(abs(self.vel_x)>0.3):
						f[0]=-45*self.vel_x
						f[1]=-0.25*self.vel_y

				elif(self.pos_x>X-0.1 and self.pos_x<X and self.pos_y<Y+0.1 and self.pos_y>Y):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = (self.pos_x-(X-0.1))/0.075
					cos = ((Y+0.1)-self.pos_y)/0.075
					self.vel_x = v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0
			
			elif(self.di==2):
				if(self.pos_x>X+0.1 and self.pos_x<X+0.15 and self.pos_y<Y and self.pos_y>Y-0.05):
					#exponential decay
					if(abs(self.vel_x)>0.3):
						f[0]=-45*self.vel_x
						f[1]=-0.25*self.vel_y

				elif(self.pos_x>X and self.pos_x<X+0.1 and self.pos_y<Y and self.pos_y>Y-0.1):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = ((X+0.1)-self.pos_x)/0.075
					cos = (self.pos_y-(Y-0.1))/0.075
					self.vel_x = -1*v*cos
					self.vel_y = -1*v*sin
					f[0]=0
					f[1]=0
			
			elif(self.di==3):
				if(self.pos_x>X-0.1 and self.pos_x<X and self.pos_y<Y-0.1 and self.pos_y>Y-0.15):
					#exponential decay
					#if(abs(self.vel_y)>0.3):
						f[1]=-45*self.vel_y
						f[0]=-25*self.vel_x

				elif(self.pos_x>X-0.1 and self.pos_x<X and self.pos_y<Y and self.pos_y>Y-0.1):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = (self.pos_x-(X-0.1))/0.075
					cos = (self.pos_y-(Y-0.1))/0.075
					self.vel_x = -1*v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0

			elif(self.di==4):
				if(self.pos_x>X and self.pos_x<X+0.1 and self.pos_y>Y+0.1 and self.pos_y<Y+0.15):
					#exponential decay
						f[1]=-45*self.vel_y
						f[0]=-25*self.vel_x

				elif(self.pos_x>X and self.pos_x<X+0.1 and self.pos_y<Y+0.1 and self.pos_y>Y):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = ((X+0.1)-self.pos_x)/0.075
					cos = ((Y+0.1)-self.pos_y)/0.075
					self.vel_x = v*cos
					self.vel_y = -1*v*sin
					f[0]=0
					f[1]=0

		elif(c==1):
			f[0]=0
			f[1]=0

		elif(c==2):
			if(self.di == 1):
				if(self.pos_x>X-0.15 and self.pos_x<X-0.12 and self.pos_y<Y+0.05 and self.pos_y>Y):
					#exponential decay
					if abs(self.vel_x)>1:
						f[0]=-60*self.vel_x
						f[1]=-0.25*self.vel_y
					elif abs(self.vel_x)<1:
						self.vel_x += 2*self.vel_x

				elif(self.pos_x>X-0.11 and self.pos_x<X+0.05 and self.pos_y>Y-0.1 and self.pos_y<Y+0.05):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					if v>1:
						v=v/1.0001
					else:
						v+= 1.5*v
					sin = (self.pos_x-(X-0.1))/0.125
					cos = (self.pos_y-(Y-0.1))/0.125
					self.vel_x = v*cos
					self.vel_y = -1*v*sin
					f[0]=0
					f[1]=0

			elif(self.di == 2):
				if(self.pos_x<X+0.15 and self.pos_x>X+0.12 and self.pos_y<Y and self.pos_y>Y-0.05):
					#exponential decay
					if abs(self.vel_x)>1:
						f[0]=-60*self.vel_x
						f[1]=-0.25*self.vel_y
					elif abs(self.vel_x)<1:
						self.vel_x += 2*self.vel_x
					
				elif(self.pos_x<X+0.11 and self.pos_x>X-0.05 and self.pos_y>Y-0.05 and self.pos_y<Y+0.1 ):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					if v>1:
						v=v/1.0001
					else:
						v+= 1.5*v
					sin = ((X+0.1)-self.pos_x)/0.125
					cos = ((Y+0.1)-self.pos_y)/0.125
					self.vel_x = -1*v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0

			elif(self.di == 3):
				if(self.pos_x<X and self.pos_x>X-0.05 and self.pos_y<Y-0.1 and self.pos_y>Y-0.15):
					if abs(self.vel_y)>1:
						f[1]=-50*self.vel_y
						f[0]=-0.25*self.vel_x
					elif abs(self.vel_y) <1:
						self.vel_y += 2*self.vel_y

				elif(self.pos_x>X-0.05 and self.pos_x<X+0.1 and self.pos_y>Y-0.1 and self.pos_y<Y+0.05):
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					if v>1:
						v=v/1.0001
					else:
						v+= 1.5*v
					sin = ((X+0.1)-self.pos_x)/0.125
					cos = (self.pos_y-(Y-0.1))/0.125
					self.vel_x = v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0

			elif(self.di == 4):
				if(self.pos_x>X and self.pos_x<X+0.05 and self.pos_y>Y+0.1 and self.pos_y<Y+0.15):
					if abs(self.vel_y)>1:
						f[1]=-50*self.vel_y
						f[0]=-0.25*self.vel_x
					elif abs(self.vel_y) <1:
						self.vel_y += 2*self.vel_y

				elif(self.pos_x<X+0.05 and self.pos_x>X-0.1 and self.pos_y<Y+0.1 and self.pos_y>Y-0.05):
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					if v>1:
						v=v/1.0001
					else:
						v+= 1.5*v
					sin = (self.pos_x-(X-0.1))/0.125
					cos = ((Y+0.1)-self.pos_y)/0.125
					self.vel_x = -1*v*cos
					self.vel_y = -1*v*sin
					f[0]=0
					f[1]=0
			
		#self.interactionDuringTurn()

		self.vel_x += f[0]*self.dt;
		self.pos_x += self.vel_x*self.dt;
		self.vel_y += f[1]*self.dt;
		self.pos_y += self.vel_y*self.dt;

	# def interactionDuringTurn():
	# 	for i in range(1):
	# 		for j in range(i+1):


	def maintSide(self, ):
		f = np.ones(2)
		f[0]=0
		f[1]=0
		X = self.currentJunc[0]
		Y = self.currentJunc[1]
		if(abs(self.vel_y)<0.2 and self.pos_y>Y and self.pos_y<Y+0.05):
			self.pos_y=Y+0.025
			#f[1]=1000*((Y+0.025)-self.pos_y)-800*self.vel_y
			f[1]=-800*self.vel_y
			f[0]=20*(self.avgVel-abs(self.vel_x))

		elif(abs(self.vel_y)<0.2 and self.pos_y<Y and self.pos_y>Y-0.05):
			self.pos_y=Y-0.025
			#f[1]=1000*((Y-0.025)-self.pos_y)-800*self.vel_y;
			f[1]=-800*self.vel_y
			f[0]=-20*(self.avgVel-abs(self.vel_x))

		elif(abs(self.vel_x)<0.2):
			if(self.pos_x>X-0.05 and self.pos_x<X):
				self.pos_x=X-0.025
				f[0]=-800*self.vel_x
				f[1]=20*(self.avgVel - abs(self.vel_y))
				#f[0]=100*((X-0.025)-self.pos_x)-800*self.vel_x
			elif((self.pos_x>X and self.pos_x<X+0.05)):
				self.pos_x=X+0.025
				f[0]=-800*self.vel_x
				f[1]=-20*(self.avgVel - abs(self.vel_y))
				#f[0]=100*((X+0.025)-self.pos_x)-800*self.vel_x
				
				



		self.vel_x += f[0]*self.dt;
		self.pos_x += self.vel_x*self.dt;
		self.vel_y += f[1]*self.dt;
		self.pos_y += self.vel_y*self.dt;