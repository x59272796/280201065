import random
wordFile = open("word.txt")
wordsList = []
for words in wordFile :
  wordsList.append(word)
word = wordsList[random.randint(0, len(wordsList) + 1)]
wordDisplay = "_ " * len(word)
counter = 5
location = 0
spec_phrase = "guess"
while counter > 0 :
  print(wordDisplay)
  print("you have " + str(counter) + " guesses left.")
  letter = input("guess a letter or type " + spec_phrase + " to guess the whole word: ")
  if letter == spec_phrase :
    guess = input("guess the word\n") 
    if guess == word :
      print("congrats, the word was indeed " + word + ".")
      break
    else :
      counter -= 1
      print("sorry, wrong guess i guess.")
  else :
    location = 0
    for words in word :
      if words == letter :
        print("great, " + letter + " was in the word. ")
        wordDisplay = wordDisplay.split(" ")
        wordDisplay[location] = letter
        wordDisplay = " ".join(wordDisplay)
      elif location + 1 == int(len(word)) and letter not in word :
        counter -=1
        print("im sorry, that was wrong :/ ")
      location += 1
  if "".join(wordDisplay.split(" ")) == word :
    print("congratulations, you won! ")
    break
print("game over! ")