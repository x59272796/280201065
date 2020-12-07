word = input("write the word ")
subString = ""
pointsWon = 0
counter1 = 0
counter2 = 0
wordsList = []
guessList = []
#player1 = str(input("player 1, write your name please: "))
#player2 = str(input("player 2, write your name please : "))
counts = 0
while True :
  counter1 = 0
  write = input("write man. ")
  for letterUp in word :
    subString = letterUp
    print(subString)
    if subString not in wordsList :
      wordsList.append(subString)
    if subString == write :
      pointsWon += 1
      if write not in guessList :
        guessList.append(write)
    for letterDown in word :
      if counter2 > counter1 :
        subString += letterDown
        print(subString)
        if subString not in wordsList :
          wordsList.append(subString)
        if subString == write :
          pointsWon += 1
          if write not in guessList :
            guessList.append(write)
      counter2 += 1
    counter1 += 1
    counter2 = 0
  print("congrats you have " + str(pointsWon))
  print(len(guessList), len(wordsList))
  if len(guessList) == len(wordsList)  :
    print("game over!")
    break