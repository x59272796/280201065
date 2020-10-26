number1 = int (input("insert number 1"))
number2 = int (input("insert number 2"))
number3 = int (input("insert number 3"))
number = number1
if number > number2 :
  if number > number3 :
    print(str(number) + "is the biggest number")
elif number < number2:
 number = number2
 if number > number3 :
   print(str(number) + "is the biggest number")
else :
  number = number3
  print(str(number) + "is the biggest number")
    