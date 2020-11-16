a = int(input("how many integers are there? "))
b = 0
while a <= 0 :
  a = int(input("please insert a positive integer number. "))
for x in range (a) :
  c = int(input("insert a number. "))
  if  c % 2 != 0 :
    b += 1
percentage = (b/a) * 100
print(str(percentage) + "%")