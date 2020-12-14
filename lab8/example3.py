import random
def get_rand_list(a,b,c) :
  randList = []
  for x in range(c) :
    d = random.randint(a,b)
    while d in randList : 
      d = random.randint(a,b)
    randList.append(d)
  return randList
def getoverlap(a,b) :
  intersection = []
  for element in a :
    if element in b :
      intersection.append(element)
  return intersection
def main() :
  firstList = get_rand_list(0,10,5)
  secondList = get_rand_list(0,10,5)
  print(getoverlap(firstList, secondList))
main()