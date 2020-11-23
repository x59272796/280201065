adress = "ceng113@example.com"
check = str(input("insert the e-mail adress to check. "))
checkLower = check.lower()
status = False
if "@" in checkLower :
  for chara in checkLower :
    if status == False :
      if chara == "." :
        print(chara)
        print(checkLower.index("."))
        checkLower.remove(chara)
        print(checkLower)
      if chara == "@" :
        status = True
if adress == checkLower :
  print("They are equal.")
else :
  print("they are not equal. ")
  
