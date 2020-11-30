group = [("Arya", 9), ("Jon", 15), ("Ned", 45), ("Bran", 10), ("Catelyn", 44)]
older = []
for tuples in group :
  if tuples[1] >= 18 :
    older.append(tuples[0])
    print(tuples[0])