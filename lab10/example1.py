def threes(n,k) :
  sum = 0
  if k != 0 :
    sum += n
    sum += threes(n,k-1)
  return sum
print(threes(3,3))