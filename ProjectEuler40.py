# We create the string where we will store the huge number and put an initial value there, so that the indexes match
integer_string = '0'
product = 1
N = [1, 10, 100, 1000, 10000, 100000, 1000000]
for digit in range(1,200000): integer_string = integer_string + str(digit)

for number in N:
    product = product * int(integer_string[number])
print(product)
