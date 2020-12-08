### Import ###
# Official
import sys
# Personal
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib
### Import ###


def toboggan_path_01(toboggan_file):
    ## Variables
    i = 1
    j = 0
    lines_01 = file_lib.read_file(toboggan_file)
    lines_02 = lines_01
    line_nb = len(lines_01)
    tree_nb = 0

    # Adding the same sring in each line each 10 lines
    for k in range(0, line_nb, 9):
        for l in range(9):
            if k + l < line_nb:
                lines_01[k + l] = lines_01[k + l] * i
                # print(lines_01[k + l])
        i += 1


    for m in range(0, line_nb * 3, 3):
        if lines_01[j][m] == '#':
            tree_nb += 1
            # print(j)
            # print('tree')

        j +=1

    print(line_nb)
    print(j)
    print(tree_nb)

    return 0

def toboggan_path_02(toboggan_file):
    ## Variables
    i = 1
    j = 0
    lines_01 = file_lib.read_file(toboggan_file)
    lines_02 = lines_01
    line_nb = len(lines_01)
    tree_nb = 0

    # Adding the same sring in each line each 10 lines. This saves hot memory
    for k in range(0, line_nb, 9):
        for l in range(9):
            if k + l < line_nb:
                lines_01[k + l] = lines_01[k + l] * i
                # print(lines_01[k + l])
        i += 1

    # Search algorithm
    for m in range(0, line_nb, 1):
        if j <= line_nb:
            if lines_01[j][m] == '#':
                tree_nb += 1
                print(j)
                print(m)
                print('tree')
                print(lines_01[j])

        j +=2

    print(line_nb)
    print(j)
    print(tree_nb)

    return 0

### Main ###
if __name__ == '__main__':
    ## Variables
    toboggan_file = '/home/the-freeman/Security/Challenges/Advent-Of-Code/Chal-03/toboggan.txt'
    lines = []
    i = 0

    toboggan_path_02(toboggan_file)























# space
