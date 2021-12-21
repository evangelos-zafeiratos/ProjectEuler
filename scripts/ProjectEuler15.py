# Calculate lattice paths for a 20x20 grid

if __name__ == "__main__":

    lattice_path_length = 20
    rows = lattice_path_length
    columns = lattice_path_length

    lattice_path = [[0 for x in range(rows)] for x in range(columns)]

    lattice_path[0][0] = 2
    for i in range(1,rows):
        for j in range(0,i+1):
            if j == i:
                lattice_path[i][j] = sum(lattice_path[i-1]) * 2
            else:
                k = j
                while k<i and k>=0:
                    lattice_path[i][j] = lattice_path[i][j] + lattice_path[i-1][k]
                    k = k - 1

    print(sum(lattice_path[lattice_path_length-1]))
