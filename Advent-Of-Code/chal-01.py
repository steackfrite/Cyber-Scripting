### Import ###
# Official
import sys
# Personal
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib
### Import ###



### Main ###
if __name__ == '__main__':
    ## Variables
    expense_file = '../../Security/Challenges/Advent-Of-Code/Chal1/list_expense.txt'
    expense_list = []
    valid_nb_list = []

    expense_list = file_lib.read_file(expense_file)
    print(expense_list)

    for i in expense_list:
        for j in expense_list:
            for k in expense_list:
                nb = int(i) + int(j) + int(k)
                if nb == 2020:
                    valid_nb_list.append(int(i) * int(j) * int(k))

    print(valid_nb_list)



















# space
