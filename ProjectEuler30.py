def fifth_powers(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)**5
    return sum

counter = 0
for i in range(2,1000000,1):
    if i == fifth_powers(i):
        counter += i

print(counter)
