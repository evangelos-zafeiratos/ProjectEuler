# Sum of all even-valued terms of the Fibonacci sequence whose values do not exceed four million.

if __name__ == "__main__":

    fib_1 = 1
    fib_2 = 2
    sum = 2
    while True:
        temp = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = temp
        if (fib_2 > 4000000):
            break
        elif (fib_2 % 2 == 0):
            sum = sum + fib_2
        print(fib_1,fib_2,sum)
    print(sum)
