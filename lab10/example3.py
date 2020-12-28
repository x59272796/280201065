def listSum(numbers) :
  sum = 0
  if len(numbers) != 0 :
    a = numbers.pop()
    if isinstance(a, int) :
      sum += a + listSum(numbers)
    elif isinstance(a, list) :
      sum += listSum(a) + listSum(numbers)
  return sum
print(listSum([3,12,76,[4,56,43],[2,8],81,75]))