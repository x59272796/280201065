password = "abc123"
tries = 3
while True :
  guess = str(input("Password:"))
  if guess == password :
    print("You have successfully logged in")
    break
  else :
    print("Sorry, the password is wrong")
    tries -= 1
  if tries <= 0 :
    print("You have been denied access")
    break
