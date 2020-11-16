password = "abc123"
a = input("Password:")
while a != password :
  if a == "help" or a == "Help" :
      print(password[0])
      a = input("Password:")
  else :
    a = input("Wrong password, please try again. ")
    
if a == password :
    print("Login successful. ")
