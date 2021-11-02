def dec_palindrome(dec_num):
    string_num = str(dec_num)
    reverse_string_num = ''
    for i in reversed(range(len(string_num))):
        reverse_string_num +=string_num[i]
    if int(reverse_string_num) == dec_num:
        return True
    else:
        return False

def bin_palindrome(binary_num):
    reverse_string_num = ''
    for i in reversed(range(len(binary_num))):
        reverse_string_num += binary_num[i]
    if binary_num == reverse_string_num:
        return True
    else:
        return False

counter = 0
for natural_number in range(1,1000000):
    binary_number = bin(natural_number)[2:]
    if dec_palindrome(natural_number) and bin_palindrome(binary_number):
        counter += natural_number

print(counter)
