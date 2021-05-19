sum_square = 0
sum = 0
for i in range(1,101):
    sum_square += i**2
    sum +=i
square_sum = sum**2
diff = square_sum - sum_square
print(diff)
