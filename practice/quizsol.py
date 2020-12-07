member_file = open('members.txt')
member_dict1 = {}
 
line = "name: email\n"
while line != "":
 name, email = line.split(':')
 member_dict1[name] = email.split('\n')[0]
 line = member_file.readline()
 
del member_dict1['name']
print(member_dict1)
member_file.close()
 
member_file = open('members.txt')
member_dict3 = {}
 
line = "xxx"
while line != "":
 if line != "xxx":
    name, email = line.split(':')
    member_dict3[name] = email[1:].split('\n')[0]
    line = member_file.readline()
 
print(member_dict3)
member_file.close()
 
member_file = open('members.txt')
member_dict2 = {}
 
while True:
 line = member_file.readline()
 if line == "":
    break
 name, email = line.split(':')
 member_dict2[name] = email.split('\n')[0]
 
print(member_dict2)
member_file.close()