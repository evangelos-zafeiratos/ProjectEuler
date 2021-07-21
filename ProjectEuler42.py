# Initialize our variables
triangle_numbers = [1]
word_counter = 0

# We populate a list with only the first 20 terms of the triangle numbers, as these should be enough
for i in range(1,20): triangle_numbers.append(triangle_numbers[i-1] + i+1)

#Open the file and create a list of strings after removing the redundant characters
fhand = open(r'C:\Users\Vangelis\Desktop\Data Science Path\Project Euler\p042_words.txt')
words_string = fhand.read()
words_string = words_string.replace('"','')
delimeter = ','
words = words_string.split(delimeter)

for word in words:
    alphabetic_value = 0
    for letter in word:
        alphabetic_value = alphabetic_value + (ord(letter) - 64)
    if alphabetic_value in triangle_numbers:
        word_counter = word_counter + 1

print(word_counter)
