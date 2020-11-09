#lab ended with example4 but i realized that there were 2 more examples leftover so these two are them
month = str(input("Please write down what month it is."))
day = input("Please write down what day it is.")
if  month == "December" or month == "december" or month == "January" or month == "january" or month == "February" or month == "february" :
  season = "Winter"
elif  month == "March" or  month == "march" or month == "April" or month == "april" or month == "May" or month == "may" :
  season = "Spring"
elif  month == "June" or month == "june"  or  month == "July" or month == "july" or month == "August" or month == "august" :  
  season = "Summer"
elif  month == "September" or month == "september"  or  month == "October" or month == "october" or month == "November" or month == "november" :
  season = "Autumn"
else  :
  month = str(input("Please write down what month it is"))
print (season, str(day), month)