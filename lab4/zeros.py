a = int(input("insert a number "))
ten = 10
numOfZeros = 0
while a % ten == 0 :
  numOfZeros += 1
  ten *= 10
print(str(a) + " has " + str(numOfZeros) + " trailing zeros.")