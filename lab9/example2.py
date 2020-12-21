def get_reversed(a) :
  if len(a) == 0 :
    return[]
  else :
    return [a.pop()] + get_reversed(a)
print(get_reversed([1,2,3,4,5]))