import math

class cylinder() :
  def __init__(self, radius, height) :
    self.radius = radius
    self.height = height
  
  def getRadius(self) :
    return self.radius

  def setRadius(self, radius) :
    self.radius = radius

  def getHeight(self) :
    return self.height

  def setHeight(self, height) :
    self.height = height

  def getArea(self) :
    return ((self.getRadius())**2) * 2 * math.pi + (self.getRadius()) * 2 * math.pi * self.getHeight() 
    
  def getVolume(self) :
    return ((self.getRadius())**2) * math.pi * self.getHeight()

radius = 3
height = 5

sample = cylinder(3,5)
