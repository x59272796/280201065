passLength = False
passUpper = False
passLower = False
passNumber = False
while passLength == False or passLower == False or passNumber == False or passUpper == False : 
  passLength = False
  passUpper = False
  passLower = False
  passNumber = False
  password = str(input("Create a password with at least: one lowercase and uppercase letter and number. "))
  if len(password) >= 8 :
    passLength = True
  for chara in password :
    if chara.isdigit() == True :
      passNumber = True
    elif chara.isupper() == True :
      passUpper = True
    elif chara.islower() == True :
      passLower = True
print("Password created successfully.")