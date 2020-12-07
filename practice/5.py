file = open("hello.txt", "r")
password = {}
a = 1
b = 1
for lines in file :
  password[lines.split("\n")[0].split(":")[0]] = lines.split("\n")[0].split(":")[1]
print(password)
name = input("whats your name my buddy? ")
while name not in password.keys() or b == 1 :
  if name in password.keys() :
    b -= 1
    passwordLogin = input("whats your password my buddy? ")
    while passwordLogin != password[name] or a == 1 :
      if passwordLogin == password[name] :
        print("login successful. ")
        a -= 1
      else :
        passwordLogin = input("worng password. whats your password again my buddy? ")
  else :
    name = input("that name is not in the list. whats your name again? ")