import math
max = 0
max_line = 1
line_number = 1

with open('p099_base_exp.txt') as f:
    for line in f:
        base, exp = line.split(",")
        number = int(exp) * math.log(int(base),10)
        if number > max:
            max = number
            max_line = line_number
        line_number +=1

print(max_line)
