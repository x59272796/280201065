def createDict(location) :
  file = open(location, "r", encoding = "utf-8")
  passDict = {}
  friendDict = {}
  for line in file :
    line = line.replace("\n", "").split(";")
    passDict[line[0]] = line[1]
    if line[2] == "" :
      friendDict[line[0]] = []
    else :
      friendDict[line[0]] = line[2].split(",")
  file.close()
  return passDict, friendDict
def update(passDict, friendDict) :
  generalList = ""
  for user in passDict :
    generalList += user + ";" + passDict[user] + ";" + ",".join(friendDict[user]) + "\n"
  return (generalList)
def login(passDict, oldUsername) :
  username = str(input("Please enter username:\n"))
  password = str(input("Please enter password:\n"))
  if username not in passDict.keys() or passDict[username] != password :
    username = oldUsername
    print("Wrong password or username\n")
  else :
    print("Logged in\n")
  return username
def validateUser(username) :
  if username != "" :
    a = True
    for character in username :
      if not (character.isdigit() or character.islower()) :
        a = False
        break
  else :
    a = False
  return a
def validatePass(password) :
  a = False
  b = False
  if len(password) >= 4 and len(password) <= 8 :
    for character in password :
      if character.isdigit() :
        a = True
      elif character.isalpha() :
        b = True
  return(a and b)
def newUser(passDict, friendDict) :
  username = str(input("Please enter username:\n"))
  if validateUser(username) and username not in passDict.keys() :
    password = str(input("Please enter password:\n"))
    if not validatePass(password) :
      print("Password not valid\n")
      password = ""
  else :
    print("Username not valid\n")
    username = ""
  if username != "" and password != "" :
    passDict[username] = password
    friendDict[username] = []
def addFriend(username, friendDict) :
  if username != "" :
    newFriend = str(input("Please enter the name of your new friend:\n"))
    if newFriend not in friendDict.keys() :
      print("Friend not found\n")
    else :
      friendDict[username].append(newFriend)
  else :
    print("You need to log in first\n")
def showFriends(username, friendDict) :
  if username != "" :
    print(",".join(friendDict[username]))
  else :
    print("You need to log in first\n")
def save(location, generalList) :
  file = open(location, "w")
  file.write(generalList)
  file.close()
def main() :
  menu_text = "1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit"
  username = "" # "" means that there is no user has logged in.
  location = "users.txt"
  passDict, friendDict = createDict(location)
  while True :
    generalList = update(passDict, friendDict)
    print(menu_text)
    operation = str(input())
    if operation == "1" :
      username = login(passDict, username)
    elif operation == "2" :
      newUser(passDict, friendDict)
    elif operation == "3" :
      addFriend(username, friendDict)
    elif operation == "4" :
      showFriends(username, friendDict)
    elif operation == "5" :
      save(location, generalList)
      break
    else :
      print("Invalid option\n")
main()