#Function to identify whether a number is palindrome or not
def is_palindrome(num):
    rev = 0
    temp_num = num
    while temp_num > 0:
        rem = temp_num % 10
        temp_num = temp_num // 10
        rev = rev*10 + rem
    if rev == num:
        return True
    else:
        return False

#Initialize our search for a = 999 and b = 999 and counting down to 900
#Flag is initialized to False. Will switch to True once the number is found and will break the nested for loop
flag = False
for number_a in range(999,900,-1):
    for number_b in range(999,900,-1):
        product = number_a*number_b
        if is_palindrome(product):
            flag = True
            break
    if flag == True:
        break

print("The number we are looking for is : " + str(product))
