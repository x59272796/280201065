class Student() :
  def __init__(self, name, grades) :
    self.name = name
    self.grades = grades

  def set_grades(self, grades) :
    self.grades = grades

  def calc_average(self) :
    return self.grades[0]*(20/100) + self.grades[1]*(20/100) + self.grades[2]*(40/100) + self.grades[3]*(10/100) + self.grades[4]*(10/100)
  # optional getters, i used them to check the grades
  def get_grades(self) :
    return self.grades

  def get_name(self) :
    return self.name

student1 = Student("yigit", [])
print(student1.get_grades())
print(student1.get_name())
student1.set_grades([80,100,60,75,55])
print(student1.get_grades())
print(student1.calc_average())