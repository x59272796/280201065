def alphanumeric(string, n) :
  non_alphanumeric = 0
  if not string[n].isalnum() :
    non_alphanumeric += 1
  if n != len(string) - 1 :
    non_alphanumeric += alphanumeric(string, n+1)
  return non_alphanumeric

def popalnum(string) :
  non_alphanumeric = 0
  string = list(string)
  if not string.pop().isalnum() :
    non_alphanumeric += 1
  if string != [] :
    non_alphanumeric += popalnum(string)
  return non_alphanumeric

#print(alphanumeric("&1ac*b1 d-4!+", 0))

print(popalnum("&1ac*b1 d-4!+"))