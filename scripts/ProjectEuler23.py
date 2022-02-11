def isAbundant(number):
    halfNumber = number // 2
    divisorList = []
    for i in range(2, halfNumber + 1):
        if number % i == 0 :
            divisorList.append(i)
        #if i == 4 and len(divisorList) == 0:
        #    return False
    #print(divisorList)
    if sum(divisorList) > number :
        return True
    else:
        return False

abundantNumbers = list()
UPPER_LIMIT = 28123
DOWN_LIMIT = 12
STEP = 1
for integerNumber in range(DOWN_LIMIT, UPPER_LIMIT, STEP):
    if isAbundant(integerNumber):
        abundantNumbers.append(integerNumber)


abundantSum = list()
for addend1 in abundantNumbers:
    for addend2 in abundantNumbers:
        sum = addend1 + addend2
        if sum < 28123:
            abundantSum.append(sum)

abundantSumSet = set(abundantSum)

totalSum = 0
for i in range(1, 28123):
    if i not in abundantSumSet:
        totalSum += i

print(totalSum)
