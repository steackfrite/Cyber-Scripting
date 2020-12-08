### Import ###
# Official
import math
import re
import sys
# Personal
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib
### Import ###

def boarding_pass_01(passport_file):
    ## Variables
    row_max = 127
    row_min = 0
    col_al_01 = 8
    col_al_02 = 0
    lines = file_lib.read_file(passport_file)
    rows = []
    columns = []

    for line in lines:
        # print(line)
        rows.append(''.join(re.findall('^([FB]{7})', line)))
        columns.append(re.findall('([LR]{3})$', line))

    for row in rows:
        row_max = 127
        row_min = 0
        for char in row:
            print(char)
            if 'F' in char:
                row_max = math.ceil((row_max - row_min) / 2)
                print('MAX')
                print(row_max)
                print(row_min)

            else:
                row_min = round(row_max / 2)
                print('MIN')
                print(row_max)
                print(row_min)

        print(row_max)

    return 0


### Main ###
if __name__ == '__main__':
    ## Variables
    boarding_file = '/home/the-freeman/Security/Challenges/Advent-Of-Code/Chal-05/boarding.txt'

    boarding_pass_01(boarding_file)























# space
