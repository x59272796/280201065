number = int(input("insert a number"))
requiredDigits = number % 100
if  requiredDigits == 0 :
  print(0)
elif requiredDigits < 10  :
  print (requiredDigits)  
elif requiredDigits < 100 :
  tens = requiredDigits // 10
  ones = requiredDigits % 10
  sum = tens + ones
  print(sum)