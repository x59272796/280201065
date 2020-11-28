equation1 = str(input("Write the first equation. "))
equation2 = str(input("Write the second equation. "))
eq1RHS = equation1.split("=")[1]
eq1LHS = equation1.split("=")[0]
eq2RHS = equation2.split("=")[1]
eq2LHS = equation2.split("=")[0]
term = ""
LHSList1 = []
RHSList1 = []
XList1 = []
YList1 = []
constantList1 = []
LHSList2 = []
RHSList2 = []
XList2 = []
YList2 = []
constantList2 = []
coefficientX1 = 0
coefficientY1 = 0
coefficientX2 = 0
coefficientY2 = 0
constant1 = 0
constant2 = 0
simplifiedEq1 = ""
simplifiedEq2 = ""
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
    XList1.append(number)
  elif element[-1] == "y" or element[-1] == "Y":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "-":
      number *= -1
    YList1.append(number)
  else:
    sign = element[0]
    element = element.replace(element[0], "")
    number = int(element)
    if sign == "+":
      number *= -1
    constantList1.append(number)
#end of LHS1
for element in RHSList1:
  sign = element[0]
  if element[-1] == "x" or element[-1] == "X":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "+":
      number *= -1
    XList1.append(number)
  elif element[-1] == "y" or element[-1] == "Y":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "+":
      number *= -1
    YList1.append(number)
  else:
    sign = element[0]
    element = element.replace(element[0], "")
    number = int(element)
    if sign == "-":
      number *= -1
    constantList1.append(number)
#end of RHS1
for numbers in XList1 :
  coefficientX1 += numbers
for numbers in YList1 :
  coefficientY1 += numbers
for numbers in constantList1 :
  constant1 += numbers
simplifiedEq1 += (str(coefficientX1) + "x")
if coefficientY1 < 0 :
  simplifiedEq1 += (str(coefficientY1) + "y") 
else :
  simplifiedEq1 += ("+" + str(coefficientY1) + "y")
simplifiedEq1 += ("=" + str(constant1))
#end of eq1
term = ""
for chara in eq2LHS:
  if chara == "+" or chara == "-":
    if term != "" :
      LHSList2.append(term)
    term = ""
  term += chara
LHSList2.append(term)
term = ""
for chara in eq2RHS:
  if chara == "+" or chara == "-":
    if term != "" :
      RHSList2.append(term)
    term = ""
  term += chara
RHSList2.append(term)
for element in LHSList2:
  sign = element[0]
  if element[-1] == "x" or element[-1] == "X":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "-":
      number *= -1
    XList2.append(number)
  elif element[-1] == "y" or element[-1] == "Y":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "-":
      number *= -1
    YList2.append(number)
  else:
    sign = element[0]
    element = element.replace(element[0], "")
    number = int(element)
    if sign == "+":
      number *= -1
    constantList2.append(number)
#end of LHS2
for element in RHSList2:
  sign = element[0]
  if element[-1] == "x" or element[-1] == "X":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "+":
      number *= -1
    XList2.append(number)
  elif element[-1] == "y" or element[-1] == "Y":
    element = element.replace(element[0], "")
    element = element.replace(element[-1], "")
    number = int(element)
    if sign == "+":
      number *= -1
    YList2.append(number)
  else:
    sign = element[0]
    element = element.replace(element[0], "")
    number = int(element)
    if sign == "-":
      number *= -1
    constantList2.append(number)
#end of RHS2
for numbers in XList2 :
  coefficientX2 += numbers
for numbers in YList2 :
  coefficientY2 += numbers
for numbers in constantList2 :
  constant2 += numbers
simplifiedEq2 += (str(coefficientX2) + "x")
if coefficientY2 < 0 :
  simplifiedEq2 += (str(coefficientY2) + "y") 
else :
  simplifiedEq2 += ("+" + str(coefficientY2) + "y")
simplifiedEq2 += ("=" + str(constant2))
#end of eq2
constantSolve = constant1
coefficientXSolve = coefficientX1
coefficientYSolve = coefficientY1
coefficientY1 *= coefficientX2
coefficientY2 *= coefficientX1
constant1 *= coefficientX2
constant2 *= coefficientX1
YFinal = int((constant1 - constant2) / (coefficientY1 - coefficientY2))
XFinal = int((constantSolve - coefficientYSolve*YFinal) / coefficientXSolve)
print("Simplified equations: ")
print(simplifiedEq1)
print(simplifiedEq2)
print("Result: ")
print("x" + "=" + str(XFinal))
print("y" + "=" + str(YFinal))