def sequence(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n = n //2
        else:
            n = 3*n + 1
        counter = counter + 1
    return counter
# We define our starting point @999999 and make the safe assumption that
# x is an odd number and 500000 < x < 999999
upper_limit = 999999
down_limit = 500000
chain_length = 0
for i in range(upper_limit,down_limit,-2):
    test = sequence(i)
    if test > chain_length:
        chain_length = test
        number = i

print(chain_length)
print(number)
