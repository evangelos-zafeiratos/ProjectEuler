#Function to identify if number is prime

if __name__ == "__main__"":

    def is_prime(x):
        for i in range (2, x//2 + 1):
            if x % i == 0:
                return False
                break
            else:
                continue
        return True

    prime_list = list()
    first_prime = 2
    prime_list.append(first_prime)
    number = 3

    while (number < 2000000) :
        if is_prime(number):
            prime_list.append(number)
        number = number + 2

    print(sum(prime_list))
