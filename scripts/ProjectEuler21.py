
# Function to calculate the sum of all divisors
def divisors_sum(n):
    sum = 0
    half_n = n//2
    if n % 2 == 0:
        for i in range(1,half_n + 1,1):
            if n % i == 0:
                sum = sum + i
    else:
        for i in range(1,half_n + 1, 2):
            if n % i == 0:
                sum = sum + i

    return sum

# Populate a list with all the divisors_sums until 10,000 using the pre-built function
upper_limit = 10000
divisors_sum_list = []
amicable_numbers_sum = 0
for i in range(upper_limit):
    divisors_sum_list.append(divisors_sum(i))

# Scan through the list to find the amicable numbers
for index in range(upper_limit):
    divisors_sum = divisors_sum_list[index]
    if divisors_sum < upper_limit and divisors_sum != index:
        if divisors_sum_list[divisors_sum] == index:
            amicable_numbers_sum = amicable_numbers_sum + divisors_sum + index

# Divide by 2 as we have calculated twice
amicable_numbers_sum = int(amicable_numbers_sum/2)
print('The total sum of all amicable numbers below 10,000 is : ', amicable_numbers_sum)
