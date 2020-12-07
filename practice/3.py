sentences = "hi! my name is yiğit. i am nearly 19. what about you damon? this is my friend russel. are we good friends? probably yes, like me and john are."
punctuations = [".", "!", "?"]
names = ["John", "Yiğit", "Damon", "Russel"]
sentences = sentences.split()
print(sentences)
sentences[0] = sentences[0].capitalize()
for a in range(len(sentences)) :
  if sentences[a][-1] in punctuations and a != len(sentences) - 1 :
    print(a)
    sentences[a+1] = sentences[a+1].capitalize()
  if sentences[a].capitalize() in names or sentences[a].capitalize().replace(sentences[a][-1], "") in names :
    sentences[a] = sentences[a].capitalize()
sentences = " ".join(sentences)
print(sentences)