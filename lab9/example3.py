def get_evens(a, i) :
  num = 0
  if a[i] % 2 == 0 :
    num += 1 
  if i != len(a) -1 :
    num += get_evens(a, i+1)
  return num
print(get_evens([0,1,2,3,4,5], 0))