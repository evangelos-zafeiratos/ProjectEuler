import math

# Optimal implementation of Eratosthenis Sieve
def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9 :
        return True
    elif n % 3 == 0:
        return False
    else:
        r = round(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f = f + 6
        return True

# Function to calculate the squre numbers multiplied by 2
def doubleSquares(n):
    return 2*(n**2)

# Function to check whether a number is composite and if yes, whether it can be
# produced as the sum of any items of our lists.
def isGoldbachNumber(primes, doubles, number):
    for prime in primes:
        for double in doubles:
            tempSum = prime + double
            if tempSum == number:
                return True
            elif tempSum > number:
                break
    print('This composite number cannot be produced as a sum: ', number)


# Initialize and populate our 2 lists. Size is estimated, arbitrarily though
primeList = list()
doubleSquareList = list()

doubleSquareListSize = 100
primeListSize = 2000


n = 0
while True:
    n += 1
    if len(primeList) == primeListSize and len(doubleSquareList) == doubleSquareListSize:
        break
    elif len(primeList) < primeListSize and len(doubleSquareList) == doubleSquareListSize:
        if isPrime(n):
            primeList.append(n)
    elif len(primeList) < primeListSize and len(doubleSquareList) < doubleSquareListSize:
        if isPrime(n):
            primeList.append(n)
        doubleSquareList.append(doubleSquares(n))

primeListSet = set(primeList)

n = 7
while True:
    n = n + 2
    if n in primeListSet:
        continue
    else:
        if not isGoldbachNumber(primeList, doubleSquareList, n):
            break
