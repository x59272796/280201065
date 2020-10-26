age = int(input("How old are you?"))
ticket = 3
discount = 50
if  age < 6 or age > 60 :
  ticket = 0
elif 6 <= age <= 18 :
  ticket = ticket * ((100 - discount)/100)
print("You have to pay " + str(ticket) + " Turkish Liras.")