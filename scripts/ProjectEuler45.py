def triangle(n):
    result = int(n*(n+1)/2)
    return result

def pentagonal(n):
    result = int(n*(3*n-1)/2)
    return result

def hexagonal(n):
    result = int(n*(2*n-1))
    return result

t_counter = 285
p_counter = 165
h_counter = 143
match = False

while match!= True:
    t_counter +=1
    value = triangle(t_counter)
    while match!= True:
        if pentagonal(p_counter) < value and hexagonal(h_counter) < value:
            p_counter +=1
            h_counter +=1
        elif pentagonal(p_counter) < value and hexagonal(h_counter) == value:
            p_counter +=1
        elif pentagonal(p_counter) < value and hexagonal(h_counter) > value:
            h_counter +=1
        elif pentagonal(p_counter) == value and hexagonal(h_counter) < value:
            h_counter +=1
        elif pentagonal(p_counter) == value and hexagonal(h_counter) == value:
            match = True
            break
        elif pentagonal(p_counter) == value and hexagonal(h_counter) > value:
            break
        elif pentagonal(p_counter) > value and hexagonal(h_counter) < value:
            h_counter +=1
        elif pentagonal(p_counter) > value and hexagonal(h_counter) == value:
            break
        elif pentagonal(p_counter) > value and hexagonal(h_counter) > value:
            break

print(value)
