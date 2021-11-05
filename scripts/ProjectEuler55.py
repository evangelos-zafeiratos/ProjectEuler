def is_lychrel(number):
    counter = 50
    while counter > 0:
        number = number + reverse(number)
        if number == reverse(number):
            return number
        counter -=1

def reverse(number):
     string_num = str(number)
     reverse_string_num = ''
     for i in reversed(range(len(string_num))):
         reverse_string_num +=string_num[i]
     reverse_number = int(reverse_string_num)
     return reverse_number

lychrel_list = []
for num in range(1,10000):
    if is_lychrel(num):
        continue
    else:
        lychrel_list.append(num)

print(len(lychrel_list))
