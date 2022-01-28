#Create a dictionary of the numbers for which we need to calculate the length

numbers = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

#This piece of code calculates the number of digits in numbers 1 - 99
total_count = 0
count = 0
for number in range (1,100,1):
    if number > 20:
        digit_1 = int(number / 10) * 10
        digit_2 = int(number % 10)
        count += len(numbers[digit_1]) + len(numbers[digit_2])
    else:
        count += len(numbers[number])


total_count = count
total_count += count + 100*len("onehundred") + 99*len("and")
total_count += count + 100*len("twohundred") + 99*len("and")
total_count += count + 100*len("threehundred") + 99*len("and")
total_count += count + 100*len("fourhundred") + 99*len("and")
total_count += count + 100*len("fivehundred") + 99*len("and")
total_count += count + 100*len("sixhundred") + 99*len("and")
total_count += count + 100*len("sevenhundred") + 99*len("and")
total_count += count + 100*len("eighthundred") + 99*len("and")
total_count += count + 100*len("ninehundred") + 99*len("and")
total_count += len("onethousand")
print(total_count)
