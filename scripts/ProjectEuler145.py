# This is a very slow implementation in Python.
# Much more efficient is the solution by hand follwing the steps:

# This problem can be solved by hand by considering what must happen for each of the possible number of digits.   For example, for a reversible number with seven digits we have:

#                  ABCDEFG
#               +  GFEDCBA

# It’s apparent that the sum of the (G,A) pairs must be odd and the sum of the (D,D) pair must be even.  Therefore, the sum of the (E,C) pairs must be > 10 to convert the column with (D,D) to an odd number.  Similarly, the sum of the (B,F) pairs must be < 10 to preserve an odd number in the (A,G) column.  Using similar reasoning, we can conclude that, for a seven-digit number, the sum of the pairs are greater than ten and odd in the first, third, fifth, and seventh columns, and less than ten and even in the other columns.  From this we can count that there are 20 possibilities for the (A,G) pairs, 25 possibilities for the (B,F) pairs, 20 possibilities for the (C,E) pairs, and 5 possibilities for the (D,D) pair.    20 x 25 x 20 x 5 = 50000.  
# Using this approach for the other digit sizes, it can be shown that the reversible number possibilities are a function of the number of digits as follows:

# nine digits       none
# eight digits    540000
# seven digits     50000
# six digits       18000
# five digits       none
# four digits        600
# three digits       100
# two digits          20

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

print(len(reversibleList))

