a = int(input("insert the first number. "))
b = int(input("insert the second number. "))
c = 10
sameDigits = 0
if a > b :
  length = len(str(b))
else :
  length = len(str(a))
for x in range(length) :
  remainder1 = a % c 
  remainder2 = b % c
  if remainder1 == remainder2 :
    sameDigits += 1
  c *= 10
print(sameDigits)