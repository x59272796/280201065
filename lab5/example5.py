#i modified this excerise to practice myself. i changed it to sum of all even fibonacci number smaller than 4mil. the original code is still there.
#num = int(input("how many fibonacci numbers would you like to generate? " ))
#while num < 2 :
  #num = int(input("how many fibonacci numbers would you like to generate? (at least 2) " ))
x = 0
a = 1
b = 2
sum = 0
fibonacci = [a,b]
evenList = [b]
#for x in range(num-2) :
while a + b < 4000000 :
  if x % 2 == 0 :
    a +=b
    fibonacci.append(a)
    if a % 2 == 0 :
      evenList.append(a)
  else :
    b +=a
    fibonacci.append(b)
    if b % 2 == 0 :
      evenList.append(b)
  x += 1
for evens in evenList :
  sum += evens
print(fibonacci)
print(evenList)
print(sum)