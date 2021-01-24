class DNA :
  def __init__(self, string) :
    string = string.upper()
    properString = True
    for nucleotide in string :
      if nucleotide != "A" and nucleotide != "T" and nucleotide != "G" and nucleotide != "C" :
        properString = False
        break
    if properString :
      self.string = string
    else :
      print("Invalid string.")

  def count_nucleotides(self) :
    nucleotideDict = {A:0, T:0, G:0, C:0}
    for nucleotide in self.string :
      nucleotideDict[nucleotide] += 1
    return nucleotideDict

  def calculate_compliment(self) :
    compliment = ""
    for nucleotide in self.string :
      if nucleotide == "A" :
        compliment += "T"
      elif nucleotide == "T" :
        compliment += "A"
      elif nucleotide == "G" :
        compliment += "C"
      elif nucleotide == "C" :
        compliment += "G"
    return compliment

  def count_point_mutations(self, muatated_string) :
    HammingDistance = 0
    for index in range(len(self.string)) :
      if self.string[index] != muatated_string[index] :
        HammingDistance += 1
    return HammingDistance





sample = DNA("GAGCC")
print(sample.count_point_mutations("CATCG"))
