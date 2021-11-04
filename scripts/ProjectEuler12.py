import math

def factor_numbers(n):
    upper_limit = int(math.sqrt(n)) + 1
    factor_list = [1]
    for i in range(2,upper_limit):
        if n % i == 0:
            factor_list.append(i)
            factor_list.append(int(n/i))
    factor_list.append(n)
    print(factor_list)
    return len(factor_list)




i = 0
number = 0
factor_length = 0

while factor_length <= 500:
    i = i+1
    number = number + i
    if number % 2 == 0:
        factor_length = factor_numbers(number)
    else:
        continue

print(number)
