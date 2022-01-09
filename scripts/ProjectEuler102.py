import numpy as np
import os

file_directory = os.getcwd() + '\p102_triangles.txt'
with open(file_directory) as reader:
    line = reader.readline()
    counter = 0
    while line != '':
        numbers = [int(number) for number in line.split(',')]
        # Calculate ab & ac vectors
        ab = [numbers[2] - numbers[0], numbers[3] - numbers[1]]
        ac = [numbers[4] - numbers[0], numbers[5] - numbers[1]]
        abxac = int(np.cross(ab,ac))

        # Calculate bc & bp vectors, where p is the (0,0) point
        bc = [numbers[4] - numbers[2], numbers[5] - numbers[3]]
        bp = [0 - numbers[2], 0 - numbers[3]]
        bcxbp = int(np.cross(bc,bp))

        # Calculate ca & cp vectors, where p is the (0,0) point
        ca = [ numbers[0] - numbers[4], numbers[1] - numbers[5]]
        cp = [0 - numbers[4], 0 - numbers[5]]
        caxcp = int(np.cross(ca,cp))

        # Calculate ab & ap vectors, where p is the (0,0) point
        ab = [numbers[2] - numbers[0], numbers[3] - numbers[1]]
        ap = [0 - numbers[0], 0 - numbers[1]]
        abxap = int(np.cross(ab,ap))

        # Set the flag to False in case there is at least one negative product
        flag = True
        if (abxac * bcxbp < 0):
            flag = False
        elif (abxac * caxcp < 0):
            flag = False
        elif (abxac * abxap < 0):
            flag = False
        if flag:
            counter +=1
        line = reader.readline()

print('The number of triangles containing point (0,0) is:', counter)
