#Function to identify if number is prime
def is_prime(x):
    for i in range (2, x//2 + 1):
        if x % i == 0:
            return False
            break
        else:
            continue
    return True

#Initialize list and assign the first value = 1 
prime_list = list()
first_prime = 2
prime_list.append(first_prime)
number = 3

while (len(prime_list) < 10001) :
    if is_prime(number):
        prime_list.append(number)
    number = number + 2

print(prime_list[10000])
