def harmonic(x) :
  sum = 1/x
  if x != 1 :
    sum += harmonic(x-1)
  return sum
print(harmonic(5))