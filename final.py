class Population :

  def __init__(self, name, size) : 
    self.name = name
    self.size = size
    self.growth_rate = 1

  def set_growth_rate(self, rate) :
    self.growth_rate = rate
    print("growth rate is set to " + str(rate))
    
  def calc_growth(self, years) :
    if years < 1 :
      return self.size
    else :
      return self.growth_rate * self.calc_growth(years - 1)

  def grow(self, years) :
    self.size *= self.growth_rate
    if years > 1 :
      return self.grow(years - 1)
    else :
      return self.size
  
  def shrink(self, number) :
    self.size -= number

def CreatePopulation(obj_name, pop_name, pop_size) :
  obj_name = Population(pop_name, pop_size)
  return obj_name

def getString(obj) :
  print(str(obj.name) + " population of size " + str(obj.size))

my_pop = CreatePopulation("my_pop", "bear", 100)
my_pop.set_growth_rate(2)
print(my_pop.calc_growth(5))
getString(my_pop)
my_pop.grow(3)
my_pop.shrink(300)
getString(my_pop)
