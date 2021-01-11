def pairStar(string, index) :
  newString = ""
  if index != len(string) - 1 :
    if string[index] == string[index + 1] :
      newString += string[index] + "*"
      newString += pairStar(string, index + 1)
    else :
      newString += string[index]
      newString += pairStar(string, index + 1)
  else :
    newString += string[-1]
  return newString

print(pairStar("hello", 0))