num = int(input("how many fibonacci numbers would you like to generate? " ))
while num < 2 :
  num = int(input("how many fibonacci numbers would you like to generate? (at least 2) " ))
a = 1
b = 1
fibonacci = [a,b]
for x in range(num) :
  if x % 2 == 0 :
    a +=b
    fibonacci.append(a)
  else :
    b +=a
    fibonacci.append(b)
print(fibonacci)