m1Weight = 30
m2Weight = 30
finalWeight = 40
studentNum = int(input("how many students are there? "))
fullList = []
average = 0
allAverage = 0
grade = 0
for x in range(studentNum) :
  m1 = int(input("insert midterm 1 grade. "))
  m2 = int(input("insert midterm 2 grade. "))
  final = int(input("insert final grade. "))
  a = [m1, m2, final]
  fullList.append(a)
  grade = (m1*m1Weight + m2*m2Weight + final*finalWeight) / 100
  average += grade
allAverage = average / studentNum
print(fullList)
print(allAverage)