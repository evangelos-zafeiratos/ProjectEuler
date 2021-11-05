# The number we are looking should be larger than already given : 918273645
# Our base number, therefore should start with the digit 9.
# Combinations for 3 digits & 1 digit have been covered. We are looking for a 4digit number, so that
# XXXX x 1 = XXXX
# XXXX x 2 = XXXXX  total number of digits = 9

# We will be starting from 9876 and counting downwards
def is_pandigital(str):
    sorted_str = ''.join(sorted(str))
    if sorted_str == '123456789':
        return True
    else:
        return False

base_number = 9876
not_found = True
while not_found:
    product_1 = base_number * 1
    product_2 = base_number * 2
    product_1_digits = str(product_1)
    product_2_digits = str(product_2)
    prod_string = product_1_digits + product_2_digits
    if is_pandigital(prod_string):
        print('EUREKA')
        not_found = False
    else:
        base_number = base_number - 1

print('The number we are looking for is : ' + str(base_number) +str(base_number * 2))
