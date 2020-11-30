employees = {}
mostEmployees = {}
salaryList = []
nameList = []
for x in range(5) :
  name = str(input("Please write the employee's name. "))
  salary = int(input("Please write the employee's salary. "))
  nameList.append(name)
  salaryList.append(salary)
  employees[name] = salary
salaryList.sort()
mostList = salaryList[-1], salaryList[-2], salaryList[-3]
for salaries in mostList :
  for employee in employees.keys() :
    if employees[employee] == salaries :
      print(employee)
      mostEmployees[employee] = salaries
print(mostEmployees)
#it doesnt handle multiple employees who get the same salary