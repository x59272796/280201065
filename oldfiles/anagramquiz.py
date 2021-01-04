def isAnagram(str1, str2) :
  str1 = str1.lower()
  str2 = str2.lower()
  anagram = True
  str1letters = []
  for letter in str1 :
    if letter not in str1letters :
      str1letters.append(letter)
  for letter in str2 :
    if letter not in str1letters :
      anagram = False
      break
  return anagram