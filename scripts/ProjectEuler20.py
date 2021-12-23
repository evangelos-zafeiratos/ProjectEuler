# Calculate the sum of the digits in the number 100!

if __name__ == '__main__':
    
    def factorial(n):
        if n == 1:
            result = 1
        else:
            result = n*factorial(n-1)
        return result

    sum = 0
    fact_100 = str(factorial(100))
    for digit in fact_100:
        sum += int(digit)
    print(sum)
