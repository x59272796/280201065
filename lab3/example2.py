number1 = int (input("insert number 1 "))
number2 = int (input("insert number 2 "))
number3 = int (input("insert number 3 "))
if  number1 < number2 :
  if number1 < number3  :
    print(str(number1) + " is the smallest number")
  else  :
    print(str(number3) + " is the smallest number")  
elif number1 > number2 :
   if number2 < number3 :
     print(str(number2) + " is the smallest number")
   else :
     print(str(number3) + " is the smallest number")  
