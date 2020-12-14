def binary_to_dec(a) :
  num = 0
  b = 1
  a = a[::-1]
  for number in a :
    if int(number) == 1 :
      print(int(number), b)
      num += int(number) * b 
    b *= 2
  return num
def dec_to_binary(a) :
  binary = ""
  while a != 0 or binary == "":
    if a % 2 == 1 :
      binary += "1"
    elif a % 2 == 0 :
      binary += "0"
    a //= 2
    binary = binary[::-1]
  return binary
print(dec_to_binary(32))