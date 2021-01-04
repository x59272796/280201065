fileStatus = False
letterStatus = False
while True :
  a = ""
  longest = ""
  letterString = ""
  if fileStatus == False :
    location = str(input("Enter a file path:"))
    fileStatus = True
  file = open(location, encoding = "utf-8")
  if letterStatus == False :
    letters = str(input("Enter a list of letters:"))
    for k in letters :
      if k.isalpha() :
        letterString += k
    while not letterString.isalpha() :
      print("Invalid input.")
      letters = str(input("Enter a list of letters:"))
      for k in letters :
        if k.isalpha() :
          letterString += k
    letters = letterString.lower()
    letters = "".join(sorted(letters))
    letterStatus = True
  merge = ""
  printList = []
  for line in file :
    currentLine = line
    currentLine = currentLine.replace(".", "").replace(",", "").replace("”", "").replace("“", "").replace("’", "").replace(".", "").replace("'", "").replace("\n", " ")
    merge += currentLine
  merge = merge.lower().split(" ")
  for letter in letters :
    longest = ""
    for word in merge :
      if letter in word :
        if len(word) > len(longest) :
          longest = word
    if longest == "" :
      a = letter + " : " + "Letter not found!"
    else :
      a = letter + " : " + longest
    if a not in printList :
      printList.append(a)
  for elements in printList :
    print(elements)
  next = input("Enter *path* for a new path, *list* for a new list of letters and *quit* to quit:")
  while next != "quit" and next != "list" and next != "path" :
    next = input("Enter *path* for a new path, *list* for a new list of letters and *quit* to quit:")
  if next == "quit" :
    print("Goodbye!")
    break
  elif next == "list" :
    letterStatus = False
  elif next == "path" :
    letterStatus = False 
    fileStatus = False
  file.close()