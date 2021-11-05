max = 0
max_a = 0
max_b = 0

for a in range(1,100,1):
    for b in range(1,100,1):
        number = a**b
        str_number = str(number)
        digits_sum = 0
        for char in str_number:
            digits_sum += int(char)
        if digits_sum > max:
            max, max_a, max_b = digits_sum, a, b

print(max,max_a,max_b)
