#you should never ever insert a negative number... i mean who can run negative miles????
initialHour = 6
initialMinute = 52
easyPaceTime = 8
tempoTime = 6
easy1 = 1
tempo1 = 3
easy2 = 2
totalTime = int (easyPaceTime * (easy1 + easy2) + (tempoTime * tempo1))
hours = int ( totalTime / 60)
minutes = int (totalTime % 60)
penultimateHours = initialHour + hours
penultimateMinutes = initialMinute + minutes
finalMinutes = int (penultimateMinutes % 60)
finalHours = int ( penultimateHours + int((penultimateMinutes / 60))) % 24
#print (str(finalHours) + ':' + str(finalMinutes))
# i wanted to solve 7:04 being showed as 7:4, disabled the first print in order to get the correct clock every time
finalMinutes2 = finalMinutes % 10
finalMinutes1 = finalMinutes // 10
print (str(finalHours) + ":" + str(finalMinutes1) + str(finalMinutes2))