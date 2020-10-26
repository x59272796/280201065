GPA = float (input("insert your GPA"))
numberOfLectures = int (input("insert your number of lectures."))
if  GPA < 2.0 :
  if  numberOfLectures < 47 :
    print("not enough GPA and lectures.")
  else  :
    print("not enough GPA.")
else  :
  if  numberOfLectures < 47 :
    print("not enough lectures.")
  else  :
    if  GPA > 4.0 :
      print("woah, i never saw a GDP higher than 4.0 before...")
    print("congratulations, you've been promoted to unemployed!!!")             