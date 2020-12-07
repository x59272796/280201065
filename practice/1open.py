import random
wordFile = open("songs.txt", "r")
wordList = []
for lines in wordFile :
  wordList.append(lines)
wordFalse = wordList[random.randint(0, len(wordList) - 1)].split("\n")
word = wordFalse[0]
found = []
tried = []
counter = 5
spec_phrase = str(input("write the special phrase with at least 2 characters to guess the whole word. "))
while len(spec_phrase) < 2 :
  spec_phrase = str(input("write the special phrase with AT LEAST 2 characters to guess the whole word. "))
while counter > 0 :
  print("you have guessed " + str(tried) + " so far.")
  currentStatus = ""
  for letter in word :
    if letter in found :
      currentStatus += letter
    elif letter == " " :
      currentStatus += " "
    else :
      currentStatus += "-"
  if currentStatus == word :
    print("congratulations, " + word + " was the word, you won!" )
    break
  print("you have " + str(counter) + " guesses left. ")
  print(currentStatus)
  guess = str(input("guess a letter or type " + spec_phrase + ", the special phrase you've set, to guess the whole word. "))
  while len(guess) != 1 and guess != spec_phrase :
    guess = str(input("guess ONLY a letter or type " + spec_phrase + ", the special phrase you've set, to guess the whole word. "))
  while guess in tried :
    guess = str(input("you have already guessed " + str(guess) + ",guess another letter or type " + spec_phrase + ", the special phrase you've set, to guess the whole word. "))
  if guess != spec_phrase :
    tried.append(guess)
  if guess in word :
    found.append(guess)
    print("congratulations! " + guess + " is in the word " + str(word.count(guess)) + " time(s).")
  elif guess == spec_phrase :
    wordGuess = str(input("guess the whole word. "))
    if wordGuess == word :
      print("congratulations, " + wordGuess + " was the word, you won!" )
      break
    else :
     print("im sorry, " + wordGuess + " wasn't the word ://")
     counter -= 1
     tried.append(wordGuess)
  else :
    print("im sorry, " + guess + " wasn't in the word ://")
    counter -= 1
  if counter <= 0 :
    print("im sorry, you are out of guesses, the word was " + str(word) + ", game over :/")