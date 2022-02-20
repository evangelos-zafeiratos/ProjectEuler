# Function to obtain the 10000 first Pentagon Numbers

def pentagonNumbers(size):
    pentagonList = []
    for i in range(1,size+1):
        nextPentagon = i*(3*i - 1)/2
        pentagonList.append(int(nextPentagon))
    return pentagonList

min = None
pentagonList = pentagonNumbers(10000)

# Allocate a set for Pentagon Numbers to speed up the searches

pentagonSet = set(pentagonList)
for i in range(len(pentagonList)//2):
    for j in range(i+1, len(pentagonList)//2):
        sum = pentagonList[i] + pentagonList[j]
        if sum < pentagonList[j+1]:
            break
        elif sum in pentagonSet:
            diff = pentagonList[j] - pentagonList[i]
            if diff in pentagonSet:
                if min == None or diff < min:
                    min = diff
                    print(i,j)

print(min)
