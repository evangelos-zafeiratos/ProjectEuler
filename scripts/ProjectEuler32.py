# Project Euler 32  - Pandigital Products
# ind the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

def multiplicand(num, digitList):
    if num < 10:
        digitList.append(num)
        #print('1st stage: ', digitList)

        return True
    elif num > 10:
        digit1 = num // 10
        digit2 = num % 10
        if digit2 == digit1 or digit2 == 0:
            #digitList.clear()
            return False
        else:
            digitList.append(digit1)
            digitList.append(digit2)
            return True

def multiplier(num, digitList):
    if num < 1000:
        digit3 = num // 100
        digit4 = (num // 10) % 10
        digit5 = num % 10
        if digit4 == 0 or digit5 == 0 or digit3 == digit4 or digit4 == digit5 or digit3 == digit5:
            return False
        elif digit3 in digitList or digit4 in digitList or digit5 in digitList:
            return False
        else:
            digitList.append(digit3)
            digitList.append(digit4)
            digitList.append(digit5)

            return True
    else:
        digit2 = num // 1000
        digit3 = (num // 100) % 10
        digit4 = (num // 10) % 10
        digit5 = num % 10
        if digit3 == 0 or digit4 == 0 or digit5 == 0 or digit2 == digit3 or digit2 == digit4 or digit2 == digit5 or digit3 == digit4 or digit3 == digit5 or digit4 == digit5:
            return False
        elif digit2 in digitList or digit3 in digitList or digit4 in digitList or digit5 in digitList:
            return False
        else:
            digitList.append(digit2)
            digitList.append(digit3)
            digitList.append(digit4)
            digitList.append(digit5)
            print('2nd stage: ', digitList)
            return True



def product(multiplicand, multiplier, digitList):
        product = multiplicand * multiplier
        if product >= 10000:
            digitList.pop(-1)
            digitList.pop(-1)
            digitList.pop(-1)
            if multiplicand < 10 :
                digitList.pop(-1)
            return 0
        digit6 = product // 1000
        digit7 = (product // 100) % 10
        digit8 = (product // 10) % 10
        digit9 = product % 10
        if digit6 == 0 or digit7 == 0 or digit8 == 0 or digit9 == 0 or digit6 == digit7 or digit6 == digit8 or digit6 == digit9 or digit7 == digit8 or digit7 == digit9 or digit8 == digit9:
            digitList.pop(-1)
            digitList.pop(-1)
            digitList.pop(-1)
            if multiplicand < 10 :
                digitList.pop(-1)
            return 0
        elif digit6 in digitList or digit7 in digitList or digit8 in digitList or digit9 in digitList:
            digitList.pop(-1)
            digitList.pop(-1)
            digitList.pop(-1)
            if multiplicand < 10 :
                digitList.pop(-1)
            return 0
        else:
            digitList.pop(-1)
            digitList.pop(-1)
            digitList.pop(-1)
            if multiplicand < 10 :
                digitList.pop(-1)
            #print(digitList)
            return product

# CASE 1 : INVESTIGATE 2-digit multiplicand x 3-digit multipliers
total_sum = 0

multiplicand_Down_Limit = 12
multiplicand_Up_Limit = 99

multiplier_Down_Limit = 123
multiplier_Up_Limit = 988
SolutionList = list()

for i in range(multiplicand_Down_Limit,multiplicand_Up_Limit):
    digitCount = list()
    if multiplicand(i, digitCount):
        for j in range(multiplier_Down_Limit, multiplier_Up_Limit):
            if multiplier(j, digitCount):
                prod = product(i,j,digitCount)
                if prod not in SolutionList:
                    SolutionList.append(prod)
                    #digitCount.clear()

# CASE 1 : INVESTIGATE 1-digit multiplicand x 4-digit multipliers
multiplicand_Down_Limit = 1
multiplicand_Up_Limit = 10

multiplier_Down_Limit = 1000
multiplier_Up_Limit = 9999
print('2nd phase')
for i in range(multiplicand_Down_Limit,multiplicand_Up_Limit):
    digitCount = list()
    if multiplicand(i, digitCount):
        for j in range(multiplier_Down_Limit, multiplier_Up_Limit):
            if multiplier(j, digitCount):
                prod = product(i,j,digitCount)
                if prod not in SolutionList:
                    SolutionList.append(prod)

print(SolutionList)
print(sum(SolutionList))
