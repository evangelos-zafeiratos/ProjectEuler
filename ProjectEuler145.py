def isReversible(num):
    if num % 10 == 0:
        return False
    strNumber = str(num)
    strReverse = strNumber[::-1]
    reverseNum = int(strReverse)
    sum = num + reverseNum
    for digit in str(sum):
        if int(digit) % 2 == 0:
            return False
    return True

reversibleList = list()
for i in range(10000000):
    if isReversible(i):
        reversibleList.append(i)

print(reversibleList)
print(len(reversibleList))
#print(isReversible(36))
#print(isReversible(37))
#print(isReversible(409))
