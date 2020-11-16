a = int(input("please insert an integer from 1 to 9 (both included). "))
b = 1
while a <= 0 or a >= 10 :
  a = int(input("please insert a positive integer. "))  
for x in range (10) :
  sum = a*b
  print(str(a) + " x " + str(b) + " = " + str(sum))
  b +=1