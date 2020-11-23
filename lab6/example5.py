matrixSize = int(input("insert the number to build a square matrix with. "))
import random #so i can build a matrix quickly
matrixList = []
counter = 0
sum = 0
for x in range(matrixSize) :
  matrix = []
  for y in range(matrixSize) :
    #matrixElement = random.randint(-9,9) # to build a quick simple matrix
    matrixElement = int(input("insert element " + str(y+1) + " to matrix " + str(x+1) + ". "))
    matrix.append(matrixElement)
    if y == counter :
      sum += matrixElement
  matrixList.append(matrix)
  counter += 1
for lists in matrixList :
  print(lists)
print(sum)