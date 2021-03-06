provincesDict = {}
provincesFile = open("provinces.txt", "r", encoding = "utf-8")
vehicleDict = {"CAR": 90, "MOTORCYCLE": 80, "BICYCLE": 25}
distanceList = []
distanceDict = {}
recommendedPlaces = []
for provinces in provincesFile :
  provinces = provinces.replace("\n", "").split(",")
  provincesDict[provinces[0]] = (float(provinces[1]), float(provinces[2]))
while True :
  departureProvince = str(input("Departure province:\n")).upper()
  length = len(departureProvince)
  possibleProvince = []
  for province in provincesDict.keys() :
    if province[0 : length] == departureProvince :
      possibleProvince.append(province)
  if departureProvince not in provincesDict.keys() :
    print("Province not found!")
    if len(possibleProvince) > 0 :
      possibleProvince.sort()
      if len(possibleProvince) == 1 :
        print("Possible province:" + ",".join(possibleProvince))
      else :
        print("Possible provinces:" + ",".join(possibleProvince))
  else :
    break
while True :
  arrivalProvince = str(input("Arrival province:\n")).upper()
  length = len(arrivalProvince)
  possibleProvince = []
  for province in provincesDict.keys() :
    if province[0 : length] == arrivalProvince :
      possibleProvince.append(province)
  if arrivalProvince not in provincesDict.keys() :
    print("Province not found!")
    if len(possibleProvince) > 0 :
      possibleProvince.sort()
      if len(possibleProvince) == 1 :
        print("Possible province:" + ",".join(possibleProvince))
      else :
        print("Possible provinces:" + ",".join(possibleProvince))
  elif arrivalProvince == departureProvince :
    print("Enter a different province!")
  else :
    break
while True :
  vehicle = str(input("Enter travel type:\n")).upper()
  if vehicle in vehicleDict.keys() :
    print("")
    break
print("I am calculating the distance between " + departureProvince + " and " + arrivalProvince + " ...\n")
distance = round((((provincesDict[arrivalProvince][0] - provincesDict[departureProvince][0])**2 + (provincesDict[arrivalProvince][1] - provincesDict[departureProvince][1])**2)**0.5)*100, 2)
print("Distance: "+ str(distance) + " km")
approxTime = distance/vehicleDict[vehicle]
hours = int(approxTime)
minutes = (approxTime - hours)*60
print("Approximate travel time with " + vehicle + ": " + str(hours) + " hours " + str(int(minutes)) + " minutes" )
for provinces in provincesDict.keys() :
  recommendedDistance = round((((provincesDict[provinces][0] - provincesDict[departureProvince][0])**2 + (provincesDict[provinces][1] - provincesDict[departureProvince][1])**2)**0.5)*100, 2)
  distanceList.append(recommendedDistance)
  distanceDict[recommendedDistance] = provinces 
distanceList.sort()
recommendedPlaces.append(distanceDict[distanceList[1]]) # index 0 gives the departure province itself
recommendedPlaces.append(distanceDict[distanceList[2]])
recommendedPlaces.append(distanceDict[distanceList[3]])
recommendedPlaces.sort()
print("Recommended places close to " + departureProvince + ":" + ",".join(recommendedPlaces))
provincesFile.close()