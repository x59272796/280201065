equation1 = str(input("Write the first equation. "))
#equation2 = str(input("Write the second equation. "))
eq1RHS = equation1.split("=")[1]
eq1LHS = equation1.split("=")[0]
#eq2RHS = equation2.split("=")[1]
#eq2LHS = equation2.split("=")[0]
term = ""
LHSList1 = []
RHSList1 = []
XList = []
YList = []
constantList = []
coefficientX = 0
coefficientY = 0
constant = 0
simplifiedEq1 = ""
for chara in eq1LHS:
  if chara == "+" or chara == "-":
    if term != "" :
      LHSList1.append(term)
    term = ""
  term += chara
LHSList1.append(term)
term = ""
for chara in eq1RHS:
  if chara == "+" or chara == "-":
    if term != "" :
      RHSList1.append(term)
    term = ""
  term += chara
RHSList1.append(term)
for element in LHSList1:
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
for element in RHSList1:
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
for numbers in XList :
  coefficientX += numbers
for numbers in YList :
  coefficientY += numbers
for numbers in constantList :
  constant += numbers
if coefficientX != 0 :
  simplifiedEq1 += (str(coefficientX) + "x ")
if coefficientY != 0 :
  if coefficientY < 0 :
    simplifiedEq1 += (str(coefficientY) + "y ") 
  else :
    simplifiedEq1 += ("+ " + str(coefficientY) + "y ")
simplifiedEq1 += ("= " + str(constant))
print(LHSList1)
print(RHSList1)
print(XList)
print(YList)
print(constantList)
print(simplifiedEq1)