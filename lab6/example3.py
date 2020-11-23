numOfInputs = int(input("how many elements would you like to insert? "))
inputList = []
outputList = []
for x in range(numOfInputs) :
  add = input("insert an element. ")
  inputList.append(add)
  if add in outputList :
    continue
  else :
    outputList.append(add)
outputList.sort()
outputList.reverse()
print(inputList)
print(outputList)