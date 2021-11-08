max = 0
for p in range(120,1001,1):
    counter = 0
    c = p//2
    while c > p//3:
        c = c-1
        a = c//2
        b = p - c - a
        while b > 1:
            if a**2 + b**2 == c**2:
                counter +=1
            a +=1
            b -=1
    print("For the perimeter value %1d there are %1d solutions" % (p,counter))
    if counter > max:
        max = counter
        perimeter_max = p


print(perimeter_max)
