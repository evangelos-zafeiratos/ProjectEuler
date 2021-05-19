#Find the prime factors for a number

div = 2
prime_factors = []
StringNumber = input('Give a number:')
number = int(StringNumber)
while number > 1:
    if number % div == 0:
        prime_factors.append(div)
        number = number / div
    #    print(prime_factors)
    elif div == 2:
        div = div + 1
    else:
        div = div + 2
print(prime_factors)
