class bird() :
  def __init__(self, color, species) :
    self.color = color
    self.species = species
  def getColor(self) :
    return self.color
  def getSpecies(self) :
    return self.species
  def getSpecial(self) :
    return str(self.color) + " " + str(self.species)

sekercik = bird("Yellow and green", "Budgie")  
print(sekercik.getSpecial())