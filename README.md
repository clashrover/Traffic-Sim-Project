# Traffic-Sim-Project
A traffic simulator using Matplotlib and numpy. Under development, will consist of cars that run as seperate processes.

Work Done Till 9/12/2019

driver file:
animation.py
  This file initialises the cars and junctions. It uses matplotlib and numpy. I plot the position of cars after each time step.
  While rest of the grid remains printed on the screen. This gives sense of animation.


class car():
  This class has functions such as maintain sides, take turn, detect turn.
  
  def maintainSide():
    This function maintains a safe distance between the edge of road and divider.
    It works as follows:
       If the car is moving in x direction then a harmonic damping force acts in y direction to not let the car deviate from the 
       equilibrium positions that i ve kept to be half og the road width.
       
  def getState():
    This function tells from where the car is coming towars the junction. The region of detection is of length 0.01 units.
    Once the state is determined (according to velocity and position) it only changes when the other state detection region 
    arrives. Thus upon arrival of new junction the state of approach of car might change.
    
  def checkInter()
    This function checks the if we have entered the region of intersection.
    
  def takeTurn():
    -According to state of approach of a car and the sequence of directions given to it initially in the constructor the car
     will take turn near the junction/intersection. 
    -As the random function was not working well with smaller number i decided to give the car sequence of turn it has
     to take to reach it's destination. 
    -When we reach a junction, it takes the value seq[i] (where i is the number of junctions it has passed) to take the necessary
     turn.
    -I was not able to give a general function that can make the car turn in specified direction so i broke up the function into
     if/else cases. There are total 6 cases with other trivial case.
     Methode is to first slow down the car using exponential decay force then let it take turn (circular) at that velocity still
     slowing the car exponentially but with less rate (I divided magnitude the tangential velocity by 0.001 at each time step).
     Rest all is use of sin and cos to make the car turn circularly.
     
   def update():
    calls all the above functions at appropriate positions.
    
class Grid():
   This class consists of juctions. Although not complete yet, but I plan to organise the juctions in an AVL tree using their
   central points as key. Using such data structure will help me detect the upcoming junction easily and fast. I will improve
   upon it and will make it static once created. This way no process will be able to alter the tree.

class Junction():
   This class' object simply plots the junction on the screen.
   It has its center point as fields. These junctions will be stored in AVL tree.
    

    
  
