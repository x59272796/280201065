class employee() :
  def __init__(self, name, salary) :
    self.name = name
    self.salary = salary

  def getName(self) :
    return self.name

  def setName(self, name) :
    self.name = name
  
  def getSalary(self) :
    return self.salary

  def setSalary(self, salary) :
    self.salary = salary

  def getInformation(self) :
    return self.name, self.salary
  
class company() :
  def __init__(self, employeeList) :
    self.employees = employeeList

  def getEmployees(self) :
    return self.employees

  def setEmployees(self, employeeList) :
    if type(employeeList) == list :
      self.employees = employeeList 

  def addEmployee(self, newEmployee) :
    if not isinstance(newEmployee, employee) :
      self.getEmployees.append(newEmployee)
    else :
      print("its not an employee")

  def averageSalary(self) :
    totalSalary = 0
    for employee in self.getEmployees() :
      totalSalary += employee.getSalary()
    return totalSalary / len(self.getEmployees())
  
  def displayEmployeeInfo(self) :
    for employee in self.getEmployees() :
      print(employee.getName(), employee.getSalary())
 
employee1 = employee("ali", 2000)
employee2 = employee("veli", 2500)
employee3 = employee("mehmet", 1500)

emptyList = []

employeeList = [employee1, employee2, employee3]

Pear = company(emptyList)
print(Pear.getEmployees())

Pear.setEmployees(employeeList)
print(Pear.getEmployees())

print(Pear.displayEmployeeInfo())
print(Pear.averageSalary())