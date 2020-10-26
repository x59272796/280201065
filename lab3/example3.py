GPA = float (input("insert your GPA"))
numberOfLectures = int (input("insert your number of lectures."))
if GPA < 2.0 :
  if numberOfLectures < 47 :
    print("not enough gpa and lectures!")
 else :
   print("not enough gpa")
elif GPA >= 2.0:
  if numberOfLectures < 47 :
    print("not enough lectures")
  else :
    print("congratulations! you've been promoted to unemployed.")        