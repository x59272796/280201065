operandsFile = open("binary.txt", "r")
bits = 32
operand = "00000000"
numberList = []
sum = 0
sumBinary = ""
while operand != "" :
  number = 0
  coef = 1
  operand = operandsFile.readline()
  if operand == "" :
    break
  operand = operand.split("\n")[0]
  for nums in operand :
    if nums != "0" and nums != "1" :
      print("wrong format")
      break
  operand = operand[::-1]
  for binary in operand :
    number += int(binary) * coef
    coef *= 2
  numberList.append(number)
print(numberList)
for numbers in numberList :
  sum += numbers
for x in range(bits-1) :
  if sum % 2 == 0 :
    sumBinary += "0"
  else :
    sumBinary += "1"
  sum //= 2
sumBinary = sumBinary[::-1]  
print(sumBinary)