import math

# Function which is based on Eratosthenis siege to calculate whether a number is prime
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

# Initiate our initial number to 11 as indicated by the exercise
# A list will be used to hold the values of truncatable numbers found and also since we search for exactly 11 elements, length of list is used in while condition
truncatable_primes = []
number = 11

while len(truncatable_primes) < 11:
    if is_prime(number):
        string_num = str(number)
        left_digit_removal = string_num
        right_digit_removal = string_num
        while True:
            left_digit_removal = left_digit_removal[1:]
            right_digit_removal = right_digit_removal[:-1]
            if is_prime(int(left_digit_removal)) and is_prime(int(right_digit_removal)):
                if len(left_digit_removal) == 1:
                    truncatable_primes.append(number)
                    break
            else:
                break
    number += 2

print(sum(truncatable_primes))
