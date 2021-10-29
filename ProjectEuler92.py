def digits_square(num):
    num_list = []
    new_num = 0
    while True:
        rem = int(num % 10)
        num_list.append(rem)
        num = num // 10
        if num == 0:
            break

    for item in num_list:
        new_num += item**2
    return new_num

count = 0
for number in range(1,10000000,1):
    while True:
        temp = digits_square(number)
        if temp == 89:
            count += 1
            break
        elif temp == 1:
            break
        else:
            number = temp

print(count)
