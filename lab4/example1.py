number = int(input("insert a number"))
requiredDigits = number % 100
if  requiredDigits == 0 :
  print(0)
elif requiredDigits < 10  and requiredDigits != 0 :
  print (requiredDigits)  
elif requiredDigits < 100 and requiredDigits >= 10  :
  tens = requiredDigits // 10
  ones = requiredDigits % 10
  sum = tens + ones
  print(sum)