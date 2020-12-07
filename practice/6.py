members = open("members.txt", "r")
memlist = {}
while True :
  a = members.readline()
  if a == "" :
    break
  a = a.split(":")
  memlist[a[0]] = a[1].split("\n")[0]
print(memlist)
print(memlist["zk"])
print(memlist.keys())