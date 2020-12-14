def sumsquare(a) :
  sum = 0
  for element in a :
    sum += element
  sum *= sum
  return sum
aList = (12,-7,5,-89.4,3,27,56,57.3)
print(sumsquare(aList))