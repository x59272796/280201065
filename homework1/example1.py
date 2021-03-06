equation1 = str(input("Enter the first equation:\n"))
equation2 = str(input("Enter the second equation:\n"))
eq1RHS = equation1.split("=")[1]
eq1LHS = equation1.split("=")[0]
eq2RHS = equation2.split("=")[1]
eq2LHS = equation2.split("=")[0]
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
coefficientX1 = coefficientY1 = coefficientX2 = coefficientY2 = constant1 = constant2 = 0
simplifiedEq1 = simplifiedEq2 = term = ""
for chara in eq1LHS: #get terms of the left hand side of eq1
  if chara == "+" or chara == "-":
    if term != "" :
      LHSList1.append(term)
    term = ""
  term += chara
LHSList1.append(term)
term = ""
for chara in eq1RHS: #get terms of the right hand side of eq1
  if chara == "+" or chara == "-":
    if term != "" :
      RHSList1.append(term)
    term = ""
  term += chara
RHSList1.append(term)
for element in LHSList1: #evaluate and organize terms of lhs1
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
for element in RHSList1: #evaluate and organize terms of rhs1
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
for numbers in XList1 : #find coefficient of x for eq1
  coefficientX1 += numbers
for numbers in YList1 : #find coefficient of y for eq1
  coefficientY1 += numbers
for numbers in constantList1 : #find constant of eq1
  constant1 += numbers
simplifiedEq1 += (str(coefficientX1) + "x") #add simplified x of eq1 to lhs
if coefficientY1 < 0 : # add simplified y of eq1 to lhs
  simplifiedEq1 += (str(coefficientY1) + "y") 
else :
  simplifiedEq1 += ("+" + str(coefficientY1) + "y")
simplifiedEq1 += ("=" + str(constant1)) #add constant of eq1 to rhs
term = ""
for chara in eq2LHS: #get terms of the left hand side of eq2
  if chara == "+" or chara == "-":
    if term != "" :
      LHSList2.append(term)
    term = ""
  term += chara
LHSList2.append(term)
term = ""
for chara in eq2RHS: #get terms of the right hand side of eq2
  if chara == "+" or chara == "-":
    if term != "" :
      RHSList2.append(term)
    term = ""
  term += chara
RHSList2.append(term)
for element in LHSList2: #evaluate and organize terms of lhs2
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
for element in RHSList2: #evaluate and organize terms of rhs2
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
for numbers in XList2 : #find coefficient of x for eq2
  coefficientX2 += numbers
for numbers in YList2 : #find coefficient of Y for eq2
  coefficientY2 += numbers
for numbers in constantList2 : #find constant for eq2
  constant2 += numbers
simplifiedEq2 += (str(coefficientX2) + "x") #add simplified x of eq2 to lhs
if coefficientY2 < 0 : #add simplified y of eq2 to lhs
  simplifiedEq2 += (str(coefficientY2) + "y") 
else : # add constant of eq2 to rhs
  simplifiedEq2 += ("+" + str(coefficientY2) + "y")
simplifiedEq2 += ("=" + str(constant2))
if coefficientX1 == 0 and coefficientY2 == 0 : #check special condition where two coefficients are zero
  YFinal = int(constant1/coefficientY1)
  XFinal = int(constant2/coefficientX2)
elif coefficientY1 == 0 and coefficientX2 == 0 :
  XFinal = int(constant1/coefficientX1)
  YFinal = int(constant2/coefficientY2)
else: #determine which equation to use for finding x
  if coefficientX1 != 0 :
    constantSolve = constant1
    coefficientXSolve = coefficientX1
    coefficientYSolve = coefficientY1
  else :
    constantSolve = constant2
    coefficientXSolve = coefficientX2
    coefficientYSolve = coefficientY2
  coefficientY1 *= coefficientX2 #solve for y and x
  coefficientY2 *= coefficientX1
  constant1 *= coefficientX2
  constant2 *= coefficientX1
  YFinal = int((constant1 - constant2) / (coefficientY1 - coefficientY2))
  XFinal = int((constantSolve - coefficientYSolve*YFinal) / coefficientXSolve)
print("Equations in the simplified form:")
print(simplifiedEq1)
print(simplifiedEq2)
print("Solution:")
print("x" + "=" + str(XFinal))
print("y" + "=" + str(YFinal))