# Function to check whether the 2 numbers have the exact same digits
def checkDigits(number1, number2):
    strNumber1 = str(number1)
    strNumber2 = str(number2)
    for digit in strNumber2:
        if digit not in strNumber1:
            return False
    return True


a = 10
found = False
while not found:
    a = a * 10
    threshold = (a * 10) // 6
    for number in range(a, threshold):
        if (checkDigits(number, number * 2)) and (checkDigits(number, number * 3)) and (checkDigits(number, number * 4)) and (checkDigits(number, number * 5)) and (checkDigits(number, number * 6)):
            print('Found! The number is : ',number)
            found = True
