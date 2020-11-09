number = int(input("insert a number"))
requiredDigits = number % 100
tens = requiredDigits // 10
ones = requiredDigits % 10
sum = tens + ones
print(sum)