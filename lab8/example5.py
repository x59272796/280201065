def securityLevel(password) :
  level = 0
  if len(password) < 8 or " " in password :
    level = 0
  else :
    alpha = False
    num = False
    special = False
    for character in password :
      if character.isalpha() :
        alpha = True
      elif character.isnumeric() :
        num = True
      else :
        special = True
    if alpha == True :
      level += 1
    if num == True :
      level += 1
    if special == True :
      level += 1
  return "Level " + str(level)
def main() :
  password = str(input("Write the password to check its security level:"))
  print(securityLevel(password))
main()