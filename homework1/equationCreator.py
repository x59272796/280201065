#this little code creates random equations
import random
x = random.randint(-99, +99)
y = random.randint(-99, +99)
print("x=" + str(x))
print("y=" + str(y))
num = int(input("insert the number of equations to the same system. "))
repeat = int(input("repeats of terms"))
for a in range(num) :
  constant = 0
  equation = ""
  for b in range(repeat) :
    coefficientX = random.randint(-1000,+1000)
    coefficientY = random.randint(-1000,+1000)
    constant += coefficientX*x + coefficientY*y
    if coefficientX >= 0 :
      equation += "+"
    equation += str(coefficientX) + "x"
    if coefficientY >= 0 :
      equation += "+"
    equation += str(coefficientY) + "y"
  equation += "="
  if constant >= 0 :
    equation += "+"
  equation += str(constant)
  print(equation)