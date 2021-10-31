def factorial(num):
    fact = 1
    while num > 1:
        fact *= num
        num = num - 1
    return fact

# According to the instructions exercise, we exclude both 1 & 2.
# Upper limit is set to 1,000,000 after trials - no theoretical proof to back this up.
upper_limit = 1000000
total_sum = 0

for number in range(3,upper_limit,1):
    string_num = str(number)
    sum = 0
    for digit in string_num:
        sum += factorial(int(digit))
    if sum == number:
        total_sum += sum
print(total_sum)
