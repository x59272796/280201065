# only pass a list youve sorted before with the selection sort algorithm
# if it returns -1, the value is not in the list.
def BinarySearch(a_list, value) :
  location = -1
  midPoint = len(a_list) // 2
  if value == a_list[midPoint] :
    location = midPoint
  elif value < a_list[midPoint] :
    location = BinarySearch(a_list[:midPoint], value)
  else :
    location = BinarySearch(a_list[midPoint + 1:], value)
  return location

a_list = [1, 3, 4, 4, 4, 8, 15, 22, 24, 26, 26, 35, 54, 59, 76, 97, 99, 548, 684]
print(BinarySearch(a_list, 97))

