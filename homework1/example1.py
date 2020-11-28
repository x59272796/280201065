equation1 = str(input("Write the first equation. "))
#equation2 = str(input("Write the second equation. "))
eq1RHS = equation1.split("=")[1]
eq1LHS = equation1.split("=")[0]
#eq2RHS = equation2.split("=")[1]
#eq2LHS = equation2.split("=")[0]
term = ""
LHSList = []
RHSList = []
XList = []
YList = []
constantList = []
for chara in eq1LHS:
  if chara == "+" or chara == "-":
    if term != "" :
      LHSList.append(term)
    term = ""
  term += chara
LHSList.append(term)
term = ""
for chara in eq1RHS:
  if chara == "+" or chara == "-":
    if term != "" :
      RHSList.append(term)
    term = ""
  term += chara
RHSList.append(term)
for element in LHSList:
  sign = element[0]
  if element[-1] == "x" or element[-1] == "X":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "-":
      number *= -1
    XList.append(number)
  elif element[-1] == "y" or element[-1] == "Y":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "-":
      number *= -1
    YList.append(number)
  else:
    sign = element[0]
    element = element.replace(element[0], "")
    number = int(element)
    if sign == "+":
      number *= -1
    constantList.append(number)
#end of LHS1
for element in RHSList:
  sign = element[0]
  if element[-1] == "x" or element[-1] == "X":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "+":
      number *= -1
    XList.append(number)
  elif element[-1] == "y" or element[-1] == "Y":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "+":
      number *= -1
    YList.append(number)
  else:
    sign = element[0]
    element = element.replace(element[0], "")
    number = int(element)
    if sign == "-":
      number *= -1
    constantList.append(number)
#end of RHS1
print(LHSList)
print(RHSList)
print(XList)
print(YList)
print(constantList)