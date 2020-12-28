def hailstone(n) :
  hailList = ""
  if n == 1 :
    return hailList + str(1)
  else :
    hailList += str(n)
    if n % 2 == 0 :
      return hailList + ", " + str(hailstone(n//2))
    else :
      return hailList + ", " + str(hailstone(3*n+1))
print(hailstone(5))