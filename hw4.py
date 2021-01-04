def printStatus(task_list, stats, heroHP, pegasusHP) : # prints current status and remaining tasks
  printHP(heroHP, pegasusHP)
  print("Here are the tasks left that hero needs to complete: ")
  print("--------------------------------------------------------")
  print("| TaskName | ByFootDistance | ByPegasus | HPNeeded |")
  print("--------------------------------------------------------")
  getTask(task_list, stats, 0) # recursive function that prints remaining tasks
  print("--------------------------------------------------------")

def printLine(task_list, stats, a, b) : # recursive function that returns lines, adjusts line size and extras to add such as km 
  string = ""
  string += "| " + task_list[a][b]  # add the first entry which is TaskName
  if b == 1 or b == 2 : # add km if its the distance column
    string += " km" + (len(stats[b]) - len(task_list[a][b]) - 4) * " " # minus 4 because there is an extra space at the beginning and adding km actually adds 3 characters with a space so we substract them from the total length so they align with their column
  else :
    string += (len(stats[b]) - len(task_list[a][b]) - 1) * " " # minus 1 because there is an extra space at the beginning so we subtract it
  if task_list[a][b] != task_list[a][-1] : # if its not the last entry in the line which is HPneeded, add the next entry to the line
    string += printLine(task_list, stats, a, b+1)
  else : # or if its the last line, just add a | to close the line
    return string + "|"
  return string

def printHall (hallstats, hallList, a, table, repeat) :
  string = ""
  if table :
    print("\n          Hall of Fame          ")
    print("--------------------------------")
    print("| Name           | Finish Time |")
    print("--------------------------------")
  string += "| " + hallList[a][0] + (len(hallstats[0]) - len(hallList[a][0]) - 5) * " "
  string += " | " + hallList[a][1] + (len(hallstats[1]) - len(hallList[a][1]) - 4) * " " + " |"
  print(string)
  print("--------------------------------")
  repeat -= 1
  if hallList[a] != hallList[-1] and repeat > 0 :
    printHall(hallstats, hallList, a+1, False, repeat)

def getTask(task_list, stats, a) : # get each task and print them in a line
  print(printLine(task_list, stats, a, 0))
  if task_list[a] != task_list[-1] :
    getTask(task_list, stats, a+1)

def printHP(heroHP, pegasusHP) :
  print("Remaining HP for Hero : " + str(heroHP))
  print("Remaining HP for Pegasus: " + str(pegasusHP) + "\n")

def askDestination(task_dict, heroHP) :
  while True :
    destination = str(input("Where should Hero go next? ")).lower().capitalize()
    if destination in task_dict.keys() :
      break
    else :
      print("Invalid input")
  if int(task_dict[destination][2]) > heroHP :
    destination == "heaven"
  return destination

def askTravel(task_dict, destination, heroHP, heroSpeed, heroHPLose, pegasusHP, pegasusSpeed, pegasusHPLose, string) :
  if (int(task_dict[destination][0]) == -1 and pegasusHP < ((int(task_dict[destination][1])/pegasusSpeed) * pegasusHPLose)) or (int(task_dict[destination][2]) > heroHP) or ((int(task_dict[destination][0]) / heroSpeed) * heroHPLose) > heroHP :
    travel = "dead"
  else :
    while True :
      travel = str(input(string)).lower().capitalize()
      if (travel == "Pegasus" and pegasusHP >= (int(task_dict[destination][1])/pegasusSpeed) * pegasusHPLose) :
        break
      elif (travel == "Foot" and int(task_dict[destination][0]) != -1) :
        if int(task_dict[destination][2]) + ((int(task_dict[destination][0]) / heroSpeed) * heroHPLose) > heroHP :
          print("Hero does not have enough HP.")
        else :
          break
      elif (travel == "Pegasus" and pegasusHP < (int(task_dict[destination][1])/pegasusSpeed) * pegasusHPLose) :
        print("Pegasus does not have enough HP.")
      elif (travel == "Foot" and int(task_dict[destination][0]) == -1) :
        print("You cannot go there by foot.")
      else :
        print("Invalid input")
  return travel

def calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed) :
  if travel == "Pegasus" :
    timeElapsed = int(task_dict[destination][1]) / pegasusSpeed
  else :
    timeElapsed = int(task_dict[destination][0]) / heroSpeed
  return int(timeElapsed)

def calculateHP(task_dict, destination, travel, quest, heroHP, pegasusHP, pegasusHPLose, heroHPLose, timeElapsed) :
  if travel == "Pegasus" :
    pegasusHP -= pegasusHPLose * timeElapsed
  else :
    heroHP -= heroHPLose * timeElapsed
  if quest == True :
    heroHP -= int(task_dict[destination][2])
  return heroHP, pegasusHP

def removeTask(task_list, task_dict, destination, n) :
  if task_list[n][0] == destination :
    task_list.pop(n)
    task_dict.pop(destination)
  else :
    removeTask(task_list, task_dict, destination, n+1)

def sortList(hallList) :
  scoreList = []
  sortedList = []
  for score in hallList :
    scoreList.append(score[1])
  scoreList.sort()
  for score in scoreList :
    for player in hallList :
      if [player[0], score] == player and [player[0], score] not in sortedList :
        sortedList.append([player[0], score])
  return sortedList

def main() :
  file = open("TaskList.txt", "r", encoding = "utf-8")
  task_list = []
  task_dict = {}
  for line in file :
    line = line.replace("\n", "").split(",")
    task_list.append(line)
    task_dict[line[0]] = [line[1], line[2], line[3]]
  file.close()
  file = open("hall_of_fame.txt", "a", encoding = "utf-8") # to make sure that a hall of fame file exists
  file.close()
  file = open("hall_of_fame.txt", "r", encoding = "utf-8")
  hallList = []
  for line in file :
    line = line.replace("\n", "").split(",")
    if line != "" :
      line[1] = int(line[1].replace(" hours", ""))
      hallList.append(line)
  print(hallList)
  file.close()
  heroHP = 3000
  heroSpeed = 20
  heroHPLose = 10
  pegasusHP = 550
  pegasusSpeed = 50
  pegasusHPLose = 15
  hours = 0
  quest = True
  home = False
  stringTravel = "How do you want to travel?(Foot/Pegasus) "
  stringHome = "How do you want to go home?(Foot/Pegasus) "
  stats = [" TaskName ", " ByFootDistance ", " ByPegasus ", " HPNeeded "] # so i can get lengths of each stat column later
  hallstats = [" | Name           |", " | Finish Time "]
  hall_of_fame_repeat = 3
  print("Welcome to Hero’s 5 Labors!")

  while True :
    if task_list != [] :
      printStatus(task_list, stats, heroHP, pegasusHP)
    else :
      print("Congratulations, you have completed the task.")
      name = str(input("What is your name : "))
      hallList.append([name, hours])
      hallList = sortList(hallList)
      for score in hallList :
        score[1] = str(score[1]) + " hours"
      hallString = ""
      file = open("hall_of_fame.txt", "w", encoding = "utf-8")
      for line in hallList :
        hallString += ",".join(line) + "\n"
      file.write(hallString)
      file.close()
      printHall(hallstats, hallList, 0, True, hall_of_fame_repeat)
      break

    destination = askDestination(task_dict, heroHP)
    if destination == "heaven" :
      print("Game over.")
      break
    travel = askTravel(task_dict, destination, heroHP, heroSpeed, heroHPLose, pegasusHP, pegasusSpeed, pegasusHPLose, stringTravel)
    if travel == "dead" :
      print("Game over.")
      break
    timeElapsed = calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed)
    heroHP, pegasusHP = calculateHP(task_dict, destination, travel, quest, heroHP, pegasusHP, pegasusHPLose, heroHPLose, timeElapsed)
    hours += timeElapsed
    if heroHP <= 0  :
      print("Game over.")
      break
    print("Hero defeated the monster.")
    print("Time passed: " + str(hours) + " hours\n")
    printHP(heroHP, pegasusHP)

    travel = askTravel(task_dict, destination, heroHP, heroSpeed, heroHPLose, pegasusHP, pegasusSpeed, pegasusHPLose, stringHome)
    if travel == "dead" :
      print("Game over.")
      break
    timeElapsed = calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed)
    hours += timeElapsed
    heroHP, pegasusHP = calculateHP(task_dict, destination, travel, home, heroHP, pegasusHP, pegasusHPLose, heroHPLose, timeElapsed)
    print("Hero arrived home.")
    print("Time passed: " + str(hours) + " hours\n")
    
    removeTask(task_list, task_dict, destination, 0)

main()