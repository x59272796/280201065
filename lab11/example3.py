class DNA :
  def __init__(self, string) :
    string = string.upper()
    properString = True
    for nucleotide in string :
      if nucleotide != "A" and nucleotide != "T" and nucleotide != "G" and nucleotide != "C" :
        properString = False
    if properString :
      self.string = string
    else :
      print("Invalid string.")

  def count_nucleotides(self) :
    A = T = G = C = 0
    for nucleotide in self.string :