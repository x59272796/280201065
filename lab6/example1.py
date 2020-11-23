adress = "ceng113@example.com"
check = str(input("insert the e-mail adress to check. "))
checkLower = check.lower()
status = False
if "@" in checkLower :
  for chara in checkLower :
    if status == False :
      if chara == "." :
        checkLower = checkLower.replace(chara , "", 1)
      if chara == "@" :
        status = True
if adress == checkLower :
  print("They are the same e-mail adress. ")
else :
  print("They are not the same e-mail adress. ")