a = [0, 16, 15, 14, 13, 12, 11, 10, 30]
i = 1
j = len(a) - 1
sum = a[i]
index = 0
while i < j and index == 0 :
  print(i)
  if sum < a[i+1] :
    print("??")
    index = i+1
  else :
    sum += a[i+1]
    i += 1
print(index)