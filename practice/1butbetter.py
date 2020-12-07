word = str(input("write the word. "))
found = []
counter = 5
spec_phrase = str(input("write the special phrase to guess the whole word. "))
while counter > 0 :
  currentStatus = ""
  for letter in word :
    if letter in found :
      currentStatus += letter
    elif letter == " " :
      currentStatus += " "
    else :
      currentStatus += "-"
  if currentStatus == word :
    print("congratulations, you won! ")
    break
  print("you have " + str(counter) + " guesses left. ")
  print(currentStatus)
  guess = str(input("guess a letter or type " + spec_phrase + ", the special phrase you've set, to guess the whole word. "))
  if guess in word :
    found.append(guess)
    print("congratulations! " + guess + " is in the word " + str(word.count(guess)) + " time(s).")
  elif guess == spec_phrase :
    wordGuess = str(input("guess the whole word. "))
    if wordGuess == word :
      print("congratulations, " + wordGuess + " was the word, you won!" )
      break
    else :
     print("im sorry," + wordGuess + " wasn't the word ://")
     counter -= 1
  else :
    print("im sorry, " + guess + " wasn't in the word ://")
    counter -= 1
  if counter <= 0 :
    print("im sorry, you are out of guesses, game over :/")