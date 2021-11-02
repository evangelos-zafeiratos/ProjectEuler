import math

#Function which is based on Eratosthenis siege to calculate whether a number is prime
def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        number = math.ceil(math.sqrt(n))
        step = 5
        while step <= number:
            if (n % step == 0) or (n % (step + 2) == 0):
                return False
                break
            step = step + 6
        return True

prime_list = []

number = 7
while sum(prime_list) < 1000000:
    if is_prime(number):
        prime_list.append(number)
    if is_prime(sum(prime_list)):
        print(sum(prime_list))
    number += 2

print(sum(prime_list))
