# only pass a list youve sorted before with the selection sort algorithm
# if it returns -1, the value is not in the list.

def BinarySearch(unsorted, num) :
  location = -1
  mid = len(unsorted) // 2
  if len(unsorted) <= 1 :
    location = -1
  else :
    if num > unsorted[mid] :
      location = BinarySearch(unsorted[mid:], num)
      if location != -1 :
        location += mid
    elif num < unsorted[mid] :
      location = BinarySearch(unsorted[:mid], num)
    elif num == unsorted[mid] :
      location = mid
  return location

my_list = [-4, 2, 7, 8, 12,22, 25, 27, 36, 42, 50, 56, 68, 85, 91, 98]

print(BinarySearch(my_list, 36))