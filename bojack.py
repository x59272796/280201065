import random
bojack_fileman = open("bojack.txt", "r")
bojack_listman = bojack_fileman.read().split(",")
bojack_fileman.close()
bojack_samplelist =  random.sample(bojack_listman, 4);
bojack = bojack_samplelist[0] + bojack_samplelist[1]
horseman = bojack_samplelist[2]
if random.randint(0,100) < 80 :
  horseman += "man"
else :
  horseman += bojack_samplelist[3]
print(bojack + " " + horseman)