# We already know that 300^2 + 400^2 = 500^2. However 300 + 400 + 500 = 1200
# We should be looking for values of 400 < c < 500 based on the initial information and estimation

c = 500
found = False
while not found:
    c = c - 1
    a = (1000 - c) // 2
    b = 1000 - c - a
    while b-a < 200:
        if (a**2 + b**2) == c**2:
            print("Eureca")
            found = True
            break
        else:
            a = a - 1
            b = b + 1
print(a*b*c)
