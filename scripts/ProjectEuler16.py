# Find the sum of the digits of the number 2^1000.

if __name__ == "__main__":

    number = 2**1000
    string = str(number)
    sum = 0

    for i in string:
        sum = sum + int(i)

    print(sum)
