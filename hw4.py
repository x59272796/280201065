def printStatus(task_list, stats) : # prints current status and remaining tasks
  printHP(heroHP, pegasusHP)
  print("--------------------------------------------------------")
  print("| TaskName | ByFootDistance | ByPegasus | HPNeeded |")
  print("--------------------------------------------------------")
  getTask(task_list, stats, 0) # recursive function that prints remaining tasks
  print("--------------------------------------------------------")

def printLine(task_list, stats, a, b) : # recursive function that returns lines, adjusts line size and extras to add such as km 
  string = ""
  string += "| " + task_list[a][b]  # add the first entry which is TaskName
  if b == 1 or b == 2 :
    string += " km" + (len(stats[b]) - len(task_list[a][b]) - 4) * " " # minus 4 because there is an extra space at the beginning and adding km actually adds 3 characters with a space so we substract them from the total length so they align with their column
  else :
    string += (len(stats[b]) - len(task_list[a][b]) - 1) * " " # minus 1 because there is an extra space at the beginning so we subtract it
  if task_list[a][b] != task_list[a][-1] : # if its not the last entry in the line which is HPneeded, add the next entry to the line
    string += printLine(task_list, stats, a, b+1)
  else : # or if its the last line, just add a | to close the line
    return string + "|"
  return string

def getTask(task_list, stats, a) : # get each task and print them in a line
  print(printLine(task_list, stats, a, 0))
  if task_list[a] != task_list[-1] :
    getTask(task_list, stats, a+1)

def printHP(heroHP, pegasusHP) :
  print("Remaining HP for Hero : " + str(heroHP))
  print("Remaining HP for Pegasus: " + str(pegasusHP))

def ask(task_dict, pegasusHP) :
  validateTask = False
  while True :
    destination = str(input("Where should Hero go next? ")).lower().capitalize()
    if destination in task_dict.keys() :
      break
    else :
      print("Invalid input")
  while True :
    travel = str(input("How do you want to travel?(Foot/Pegasus) ")).lower().capitalize()
    if (travel == "Pegasus" and pegasusHP != 0) :
      break
    elif (travel == "Foot" and int(task_dict[destination][0]) != -1) :
      break
    elif (travel == "Pegasus" and pegasusHP == 0) :
      print("Pegasus does not have enough HP.")
    elif (travel == "Foot" and int(task_dict[destination][0]) == -1) :
      print("You cannot go there by foot.")
    else :
      print("Invalid input")
  return destination, travel

def calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed) :
  if travel == "Pegasus" :
    timeElapsed = int(task_dict[destination][1]) / pegasusSpeed
  else :
    timeElapsed = int(task_dict[destination][0]) / heroSpeed
  return int(timeElapsed)

file = open("TaskList.txt", "r", encoding = "utf-8")
task_list = []
task_dict = {}
for line in file :
  line = line.replace("\n", "").split(",")
  task_list.append(line)
  task_dict[line[0]] = [line[1], line[2], line[3]]
file.close()
heroHP = 3000
heroSpeed = 20
pegasusHP = 550
pegasusSpeed = 50
hours = 0
stats = [" TaskName ", " ByFootDistance ", " ByPegasus ", " HPNeeded "] # so i can get lengths of each stat column later
print("Welcome to Hero’s 5 Labors!")
while True :
  printStatus(task_list, stats)
  destination, travel = ask(task_dict, pegasusHP)
  hours += calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed)
  print(hours)