### Import ###
# Official
import sys
# Personal
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib
### Import ###


def policy_01(pwd_file):
    i = 0
    lines = file_lib.read_file(pwd_file)

    for line in lines:
        line_split = line.split(':')
        pwd = line_split[1].replace(' ', '')
        policy_interval = line_split[0].split(' ')
        char_pwd = policy_interval[1]
        min_rep = policy_interval[0].split('-')[0]
        max_rep = policy_interval[0].split('-')[1]
        rep = pwd.count(char_pwd)

        if rep >= int(min_rep) and rep <= int(max_rep):
            i += 1
        # print(line_split)

    print(i)

    return 0

def policy_02(pwd_file):
    i = 0
    lines = file_lib.read_file(pwd_file)

    for line in lines:
        line_split = line.split(':')
        pwd = line_split[1].replace(' ', '')
        policy_interval = line_split[0].split(' ')
        char_pwd = policy_interval[1]
        first_occu = policy_interval[0].split('-')[0]
        second_occu = policy_interval[0].split('-')[1]
        # rep = pwd.count(char_pwd)

        if pwd[int(first_occu) - 1 ] == char_pwd and pwd[int(second_occu) - 1 ] != char_pwd:
            i += 1
            print(line)
        elif pwd[int(first_occu) - 1 ] != char_pwd and pwd[int(second_occu) - 1 ] == char_pwd:
            i += 1
            print(line)
        # print(line_split)
        # print(pwd.find('char_pwd') + 1)

    print(i)

    return 0

### Main ###
if __name__ == '__main__':
    ## Variables
    pwd_file = '../../Security/Challenges/Advent-Of-Code/Chal-02/pwd_list.txt'
    lines = []
    i = 0

    policy_02(pwd_file)























# space
