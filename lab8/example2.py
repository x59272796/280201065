def is_prime(a) :
  status = True
  for x in range(2,a) :
    if a % x == 0 :
      status = False
      break
  return status
def print_primes_between(a,b) :
  primeList = []
  for x in range(a,b) :
    if is_prime(x) :
      primeList.append(x)
  print(primeList)
def main() :
  first = int(input("Write the first integer. "))
  second = int(input("Write the second integer. "))
  print_primes_between(first,second)
main()