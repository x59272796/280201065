import time
def countdown(t) :
  if t == 0 :
    print("Time's up!")
  else :
    print(t)
    time.sleep(1)
    countdown(t-1)
countdown(5)