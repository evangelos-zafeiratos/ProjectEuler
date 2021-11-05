number = 2520
found = False
while found != True:
    for i in range(1,21):
        if number % i != 0:
            number = number + 20
            break
        elif number % i == 0:
            if i==20:
                found = True
                break
            else:
                continue
print(number)
