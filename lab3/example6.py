A = int(input("please insert the coefficient of X^2"))
B = int(input("please insert the coefficient of x"))
C = int(input("please insert the number c"))
delta = B**2 - 4*A*C
if  delta > 0 :
  root1 = (-B + delta) / 2*A
  root2 = (-B - delta) / 2*A
  print(root1, root2)
elif delta == 0 :
  root1 = -B/2*A
  print(root1)
elif delta < 0  :
  print("no real roots.")