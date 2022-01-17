# Project Euler 29
# Calculate all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

numberList = list()
if __name__ == "__main__":
    for a in range(2,101,1):
        for b in range(2,101,1):
            if a**b not in numberList:
                numberList.append(a**b)
            else:
                continue

print(len(numberList))
