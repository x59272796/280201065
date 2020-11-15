a = int(input("insert a positive integer. "))
sum = 1
while a < 0 :
  a = int(input("we can't calculate the factorial of a negative integer, please insert a positive integer. "))
initialNum = a
while a > 1 :
  sum *= a
  a -= 1
print(str(initialNum) + "!" + " equals to " + str(sum))