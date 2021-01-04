def square(x) :
  return x*x

print(square(2))
print(square(10))
a = 2
print(square(square(square(a))))

def add(x,y,z) :
  return x+y+z

def multiply(x,y) :
  return x*y

print(add(1,2,3))
print(multiply(3,5))
a = 2 
b = 3

import random

def roll_dice() :
  return random.randint(1,6)

def lucky(lucky_number) :
  a = roll_dice()
  if a != lucky_number :
    print(a)
    lucky(lucky_number)
  
lucky(6)