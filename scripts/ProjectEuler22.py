def calculate_value(name):
    score = 0
    for char in name:
        score += ord(char) - 64
    return(score)

total_score = 0
with open(r'C:\Users\Vangelis\Desktop\Data Science Path\Project Euler\p022_names.txt') as f:
    names_file = f.read().replace('"','').split(",")
    names_file.sort()
    for i in range (0,len(names_file),1):
        total_score = total_score + calculate_value(names_file[i])*(i+1)

    print(total_score)
