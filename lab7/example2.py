books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
bookDict = {}
for book in books :
  uniqueChara =[]
  for chara in book :
    if chara in uniqueChara :
      continue
    else  :
      uniqueChara.append(chara)
  length = len(book)
  unique = len(uniqueChara)
  average = int((length + unique) / 2)
  bookDict[book] = (length,unique,average)
print(bookDict)