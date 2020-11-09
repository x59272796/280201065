number = str(input("insert a number"))
for digits in number:
  if digits != len(number) - 1 or digits != len(number) - 2 :
    continue
  elif digits == len(number) - 2 :
    tens = int(digits)
    continue
  elif digits == len(number) - 1  :
    ones = int(digits)
  else  :
    continue
sum = tens + ones
print(sum)