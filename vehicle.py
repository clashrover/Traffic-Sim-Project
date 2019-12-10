import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import math

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
	def __init__(self, pos_x, pos_y, vel_x, vel_y,cars):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.seq.append(0)
		self.di = 0
		self.cars = cars

	def reset(self,):
		self.vel_x=0
		self.vel_y=0

	# def setList(self,cars):
	# 	list = cars

	def update(self, ):
		if(self.checkInter()):
			self.takeTurn()
		else:
			self.maintSide()
			#self.checkBoundary()

	def checkInter(self, ):
		return bool(self.pos_y<0.7 and self.pos_y>0.3 and self.pos_x<0.7 and self.pos_x>0.3)

	def getState(self, ):
		if(self.pos_x<0.35 and self.pos_x>0.34 and abs(self.vel_y)<0.2 and self.vel_x>0.2):
			self.di = 1
		elif(self.pos_x>0.65 and self.pos_x<0.66 and abs(self.vel_y)<0.2 and self.vel_x<-0.2):
			self.di = 2
		elif(self.pos_y<0.35 and self.pos_y>0.34 and abs(self.vel_x)<0.2 and self.vel_y>0.2):
			self.di = 3
		elif(self.pos_y>0.65 and self.pos_y<0.66 and abs(self.vel_x)<0.2 and self.vel_y<-0.2):
			self.di = 4
		
	def takeTurn(self, ):
		c = self.seq[0]
		f = np.ones(2)
		self.getState()
		 
		if(c==0):
			if(self.di==1):
				if(self.pos_x>0.35 and self.pos_x<0.39 and self.pos_y<0.55 and self.pos_y>0.5):
					#exponential decay
					if(abs(self.vel_x)>0.3):
						f[0]=-75*self.vel_x
						f[1]=-0.25*self.vel_y

				elif(self.pos_x>0.4 and self.pos_x<0.5 and self.pos_y<0.6 and self.pos_y>0.5):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = (self.pos_x-0.4)/0.075
					cos = (0.6-self.pos_y)/0.075
					self.vel_x = v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0
			
			elif(self.di==2):
				if(self.pos_x>0.6 and self.pos_x<0.65 and self.pos_y<0.5 and self.pos_y>0.45):
					#exponential decay
					if(abs(self.vel_x)>0.3):
						f[0]=-75*self.vel_x
						f[1]=-0.25*self.vel_y

				elif(self.pos_x>0.5 and self.pos_x<0.6 and self.pos_y<0.5 and self.pos_y>0.4):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = (0.6-self.pos_x)/0.075
					cos = (self.pos_y-0.4)/0.075
					self.vel_x = -1*v*cos
					self.vel_y = -1*v*sin
					f[0]=0
					f[1]=0
			
			elif(self.di==3):
				if(self.pos_x>0.4 and self.pos_x<0.5 and self.pos_y<0.4 and self.pos_y>0.35):
					#exponential decay
					#if(abs(self.vel_y)>0.3):
						f[1]=-75*self.vel_y
						f[0]=-25*self.vel_x

				elif(self.pos_x>0.4 and self.pos_x<0.5 and self.pos_y<0.5 and self.pos_y>0.4):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = (self.pos_x-0.4)/0.075
					cos = (self.pos_y-0.4)/0.075
					self.vel_x = -1*v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0

			elif(self.di==4):
				if(self.pos_x>0.5 and self.pos_x<0.6 and self.pos_y>0.6 and self.pos_y<0.65):
					#exponential decay
						f[1]=-75*self.vel_y
						f[0]=-25*self.vel_x

				elif(self.pos_x>0.5 and self.pos_x<0.6 and self.pos_y<0.6 and self.pos_y>0.5):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					sin = (0.6-self.pos_x)/0.075
					cos = (0.6-self.pos_y)/0.075
					self.vel_x = v*cos
					self.vel_y = -1*v*sin
					f[0]=0
					f[1]=0

		elif(c==1):
			f[0]=0
			f[1]=0

		elif(c==2):
			if(self.di == 1):
				if(self.pos_x>0.35 and self.pos_x<0.38 and self.pos_y<0.55 and self.pos_y>0.5):
					#exponential decay
					f[0]=-90*self.vel_x
					f[1]=-0.25*self.vel_y
				elif(self.pos_x>0.39 and self.pos_x<0.55 and self.pos_y>0.4 and self.pos_y<0.55 ):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					v=v/1.0001
					sin = (self.pos_x-0.4)/0.125
					cos = (self.pos_y-0.4)/0.125
					self.vel_x = v*cos
					self.vel_y = -1*v*sin
					f[0]=0
					f[1]=0

			elif(self.di == 2):
				if(self.pos_x<0.65 and self.pos_x>0.62 and self.pos_y<0.5 and self.pos_y>0.45):
					#exponential decay
					f[0]=-90*self.vel_x
					f[1]=-0.25*self.vel_y
				elif(self.pos_x<0.61 and self.pos_x>0.45 and self.pos_y>0.45 and self.pos_y<0.6 ):
					#circular force
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					v=v/1.0001
					sin = (0.6-self.pos_x)/0.125
					cos = (0.6-self.pos_y)/0.125
					self.vel_x = -1*v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0

			elif(self.di == 3):
				if(self.pos_x<0.5 and self.pos_x>0.45 and self.pos_y<0.4 and self.pos_y>0.35):
					f[1]=-50*self.vel_y
					f[0]=-0.25*self.vel_x
				elif(self.pos_x>0.45 and self.pos_x<0.6 and self.pos_y>0.4 and self.pos_y<0.55):
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					v=v/1.0001
					sin = (0.6-self.pos_x)/0.125
					cos = (self.pos_y-0.4)/0.125
					self.vel_x = v*cos
					self.vel_y = v*sin
					f[0]=0
					f[1]=0

			elif(self.di == 4):
				if(self.pos_x>0.5 and self.pos_x<0.55 and self.pos_y>0.6 and self.pos_y<0.65):
					f[1]=-50*self.vel_y
					f[0]=-0.25*self.vel_x
				elif(self.pos_x<0.55 and self.pos_x>0.4 and self.pos_y<0.6 and self.pos_y>0.45):
					v = math.sqrt((self.vel_y*self.vel_y)+(self.vel_x*self.vel_x))
					v=v/1.0001
					sin = (self.pos_x-0.4)/0.125
					cos = (0.6-self.pos_y)/0.125
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
		if(self.vel_y<0.5 and self.vel_y>-0.5 and self.pos_y>0.5 and self.pos_y<0.55):
			f[1]=100*(0.525-self.pos_y)-800*self.vel_y;
		elif(self.vel_y<0.5 and self.vel_y>-0.5 and self.pos_y<0.5 and self.pos_y>0.45):
			f[1]=100*(0.475-self.pos_y)-800*self.vel_y;

		elif(self.vel_x<0.5 and self.vel_x>-0.5):
			if(self.pos_x>0.45 and self.pos_x<0.5):
				f[0]=100*(0.475-self.pos_x)-800*self.vel_x
			elif((self.pos_x>0.5 and self.pos_x<0.55)):
				f[0]=100*(0.525-self.pos_x)-800*self.vel_x



		self.vel_x += f[0]*self.dt;
		self.pos_x += self.vel_x*self.dt;
		self.vel_y += f[1]*self.dt;
		self.pos_y += self.vel_y*self.dt;