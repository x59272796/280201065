numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
intersection = []
union = []
numbers1Set = set(numbers1)
numbers2Set = set(numbers2)
for number in numbers1Set :
  if not number in union :
    union.append(number)
  for numbers in numbers2Set :
    if number == numbers :
      intersection.append(number)
    if not numbers in union :
      union.append(numbers)
print("The intersection set is" + str(set(intersection)))
print("The union set is" + str(set(union)))