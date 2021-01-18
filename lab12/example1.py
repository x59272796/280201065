def SelectionSort(unsorted) :
  for i in range (len(unsorted)) :
    minIndex = i
    for x in range(i, len(unsorted)) :
      if unsorted[minIndex] > unsorted[x] :
        minIndex = x
    if minIndex != i :
      unsorted[i], unsorted[minIndex] = unsorted[minIndex], unsorted[i]
  return unsorted

a = [15, 26, 8, 26, 548, 4, 1, 3, 99, 4, 97, 24, 54, 76, 22, 35, 4, 59, 684]
a = SelectionSort(a)
print(a)