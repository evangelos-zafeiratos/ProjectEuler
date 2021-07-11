#Fibonacci initial numbers
fib_1 = 1
fib_2 = 1
index = 2

while True:
    fib_number = fib_1 + fib_2
    index +=1
    if len(str(fib_number)) < 1000:
        fib_1 = fib_2
        fib_2 = fib_number
    elif len(str(fib_number)) == 1000:
        break
    else:
        print("Could not find digit with precisely 1000 digits.")
        break

print(index)
