# ProjectEuler24 - Lexicographic permutations

numList = [i for i in range(0,10)]
firstDigit = 0
oneBeforelastDigit = len(numList) - 2
lastDigit = len(numList) - 1


for i in range(1000000): #
    print("Iteration No:",i+1, "list is: ", numList)
    # Iterate through the digits of the string
    for pos in range(oneBeforelastDigit, firstDigit-1,-1):
        if numList[pos] < numList[pos+1]:
            shortList = [numList[i] for i in range(pos+1, lastDigit+1)]
            shortList = sorted(shortList)
            for index, value in enumerate(shortList):
                #print(value, shortList)
                if value > numList[pos]:
                    temp = shortList.pop(index)
                    shortList.append(numList[pos])
                    numList[pos] = temp
                    break
            shortList = sorted(shortList)
            numList = numList[:pos+1] + shortList
        else:
            continue
        break

print(numList)
