sum = 0
for i in range(1,1001):
    sum += pow(i,i)
    #print(i)
string_sum = str(sum)
for i in range(-10,0):
    print(string_sum[i],end = '')
