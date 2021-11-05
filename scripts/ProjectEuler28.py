series_1 = [1]
series_2 = [1]
series_3 = [1]
series_4 = [1]
for i in range(500):
    series_1_next = series_1[i] + 8*(i+2) - 14
    series_2_next = series_2[i] + 8*(i+2) - 12
    series_3_next = series_3[i] + 8*(i+2) - 10
    series_4_next = series_4[i] + 8*(i+2) - 8
    series_1.append(series_1_next)
    series_2.append(series_2_next)
    series_3.append(series_3_next)
    series_4.append(series_4_next)

print(series_1)
print(series_3)
print(sum(series_1) + sum(series_2) + sum(series_3) + sum(series_4))
