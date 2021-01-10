#280201065

def printStatus(task_list, stats, heroHP, pegasusHP) : # prints current status and remaining tasks
  printHP(heroHP, pegasusHP)
  print("Here are the tasks left that hero needs to complete: ")
  print("----------------------------------------------------")
  print("| TaskName | ByFootDistance | ByPegasus | HPNeeded |")
  print("----------------------------------------------------")
  print_remaining_tasks(task_list, stats, 0) # recursive function that prints remaining tasks
  print("----------------------------------------------------")

def printLine(task_list, stats, a, b) : # recursive function that returns lines, adjusts line size and extras to add such as km, stats is used to determine the length of each row entry, a is task index and b is index of each attribute of that task
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

def printHall (hallstats, hallList, player, table, repeat) : # prints the hall of fame with the specified repeat time, hallstats helps me determine the length of the table, hallList is the list with the high scores and players, player is entry number of a player, table is if we are first printing "hall of fame" and name/finish time, repeat is the number of players to show in the table
  string = ""
  if table : #use it when printing the table for the first time
    print("\n          Hall of Fame          ") # header
    print("--------------------------------")
    print("| Name           | Finish Time |")
    print("--------------------------------")
  string += "| " + hallList[player][0] + (len(hallstats[0]) - len(hallList[player][0]) - 5) * " " # like with the function above, aligns the text
  string += " | " + hallList[player][1] + (len(hallstats[1]) - len(hallList[player][1]) - 4) * " " + " |"
  print(string)
  print("--------------------------------")
  repeat -= 1
  if hallList[player] != hallList[-1] and repeat > 0 :
    printHall(hallstats, hallList, player+1, False, repeat) # print the next entry in a recursive manner

def print_remaining_tasks(task_list, stats, a) : # get each task and print them in a line, stats is used to get the length of each row entry and a is used to get the index of task
  print(printLine(task_list, stats, a, 0))
  if task_list[a] != task_list[-1] :
    print_remaining_tasks(task_list, stats, a+1) # recursive part

def printHP(heroHP, pegasusHP) : # prints hps of hero and pegasus
  print("Remaining HP for Hero : " + str(heroHP))
  print("Remaining HP for Pegasus: " + str(pegasusHP) + "\n")

def askDestination(task_dict, heroHP) : #asks where to go
  while True :
    destination = str(input("Where should Hero go next? ")).lower().capitalize()
    if destination in task_dict.keys() :
      break
    else :
      print("Invalid input")
  if int(task_dict[destination][2]) > heroHP :
    destination == "heaven" # heaven is a silly way to sign that the game over conditions are fulfilled
  return destination

def askTravel(task_dict, destination, heroHP, heroSpeed, heroHPLose, pegasusHP, pegasusSpeed, pegasusHPLose, string) : #ask how to go to a destination and determine if the game will continue, parameters are kind of self explanatory, string is the question where we ask the player how to go home or to the quest
  if (int(task_dict[destination][0]) == -1 and pegasusHP < ((int(task_dict[destination][1])/pegasusSpeed) * pegasusHPLose)) or (((int(task_dict[destination][0]) / heroSpeed) * heroHPLose) > heroHP and pegasusHP < ((int(task_dict[destination][1])/pegasusSpeed) * pegasusHPLose)) : # fail conditions, if the destination is unreachable on foot and pegasus has insufficient hp OR both the hero and pegasus have insufficient hp to travel
    travel = "dead" # dead is a silly way to sign that the game is over.
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

def calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed) : # calculate the time with these given parameters
  if travel == "Pegasus" :
    timeElapsed = int(task_dict[destination][1]) / pegasusSpeed
  else :
    timeElapsed = int(task_dict[destination][0]) / heroSpeed
  return int(timeElapsed)

def calculateHP(task_dict, destination, travel, quest, heroHP, pegasusHP, pegasusHPLose, heroHPLose, timeElapsed) : # calculate the remaining hp, quest is if the hero has fought a monster or not
  if travel == "Pegasus" :
    pegasusHP -= pegasusHPLose * timeElapsed
  else :
    heroHP -= heroHPLose * timeElapsed
  if quest == True :
    heroHP -= int(task_dict[destination][2])
  return heroHP, pegasusHP

def removeTask(task_list, task_dict, destination, n) : #remove tasks in a recursive manner
  if task_list[n][0] == destination :
    task_list.pop(n)
    task_dict.pop(destination)
  else :
    removeTask(task_list, task_dict, destination, n+1)

def sortList(hallList) : # a function to sort a list with their second entry. instead of using a lambda key inside sort(), i felt more comfortable implementing a function like that
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
  # we initialize the game from here to the starting string
  file = open("TaskList.txt", "r", encoding = "utf-8")
  hall_of_fame_location = "hall_of_fame.txt" # modify this string to change the hall of fame file location
  task_list = []
  task_dict = {}
  for line in file : # get each task to a list and a dictionary
    line = line.replace("\n", "").split(",")
    task_list.append(line)
    task_dict[line[0]] = [line[1], line[2], line[3]]
  file.close()
  file = open(hall_of_fame_location, "a", encoding = "utf-8") # to make sure that a hall of fame file exists, appending creates the file if it doesnt exist
  file.close()
  file = open(hall_of_fame_location, "r", encoding = "utf-8")
  hallList = []
  for line in file : # add each entry in the hall of fame to a list
    line = line.replace("\n", "").split(",")
    if line != "" :
      line[1] = int(line[1].replace(" hours", "")) # to compare hours as integers, we have the remove the hours prefix at each entry
      hallList.append(line)
  file.close()

  heroHP = 3000
  heroSpeed = 20
  heroHPLose = 10
  pegasusHP = 550
  pegasusSpeed = 50
  pegasusHPLose = 15
  hours = 0
  quest = True # to input into askTravel(), makes it easier to see where the hero is going
  home = False # to input into askTravel(), makes it easier to see where the hero is going
  stringTravel = "How do you want to travel?(Foot/Pegasus) " #string to ask while going on a task
  stringHome = "How do you want to go home?(Foot/Pegasus) " #string to ask while returning home
  stats = [" TaskName ", " ByFootDistance ", " ByPegasus ", " HPNeeded "] # so i can get lengths of each stat column
  hallstats = [" | Name           |", " | Finish Time "] # to get lengths of hall of fame table columns
  hall_of_fame_repeat = 3 # how many players to show on the hall of fame

  print("Welcome to Hero’s 5 Labors!") # starting text
  # game loop begins here
  while True :
    if task_list != [] : #if tasks are not over, go with the usual flow of the game
      printStatus(task_list, stats, heroHP, pegasusHP)
    else : # if tasks are over, take name as an input, add them to the hall of fame, print the hall of fame and quit
      print("Congratulations, you have completed the task.")
      name = str(input("What is your name : "))
      hallList.append([name, hours]) #add entry
      hallList = sortList(hallList) #sort the hall of fame with hours ascending
      for score in hallList :
        score[1] = str(score[1]) + " hours" # add the hours prefix to each entry
      hallString = ""
      file = open("hall_of_fame.txt", "w", encoding = "utf-8")
      for line in hallList :
        hallString += ",".join(line) + "\n"
      file.write(hallString) # write the new hall of fame to the file
      file.close()
      printHall(hallstats, hallList, 0, True, hall_of_fame_repeat) #print the hall of fame
      break
    # game phase one where you ask the user to go on a quest
    destination = askDestination(task_dict, heroHP) # ask where to go
    if destination == "heaven" : # a silly way to determine if the game is over
      print("Game over.")
      break
    travel = askTravel(task_dict, destination, heroHP, heroSpeed, heroHPLose, pegasusHP, pegasusSpeed, pegasusHPLose, stringTravel) # ask how to go to the task
    if travel == "dead" or destination == "heaven" : # a silly way to determine if the game is over
      print("Game over.")
      break
    timeElapsed = calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed)
    heroHP, pegasusHP = calculateHP(task_dict, destination, travel, quest, heroHP, pegasusHP, pegasusHPLose, heroHPLose, timeElapsed) # calculate hp and time
    hours += timeElapsed
    if heroHP < 0  : # if the hero has less than 0 hp, end the game
      print("Game over.")
      break
    print("Hero defeated the monster.")
    print("Time passed: " + str(hours) + " hours\n")
    printHP(heroHP, pegasusHP)
    # game phase two where you return home
    travel = askTravel(task_dict, destination, heroHP, heroSpeed, heroHPLose, pegasusHP, pegasusSpeed, pegasusHPLose, stringHome) #ask how to return home
    if travel == "dead" or heroHP < 0 :
      print("Game over.")
      break
    timeElapsed = calculateTime(task_dict, destination, travel, heroSpeed, pegasusSpeed)
    hours += timeElapsed
    heroHP, pegasusHP = calculateHP(task_dict, destination, travel, home, heroHP, pegasusHP, pegasusHPLose, heroHPLose, timeElapsed)
    print("Hero arrived home.")
    print("Time passed: " + str(hours) + " hours\n")
    
    removeTask(task_list, task_dict, destination, 0)
    # game loop ends here

main()