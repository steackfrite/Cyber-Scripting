#!/usr/bin/python
## Import ##
import sys
# Perso
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib

def digits_of(n):
    return [int(d) for d in str(n)]

def luhn_checksum(card_number):

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


### Main ###
if __name__ == '__main__':

    prefix = 543210
    suffix = 1234

    for i in range(100000, 999999):
        final_num = str(prefix) + str(i) + str(suffix)
        if is_luhn_valid(int(final_num)) and (int(final_num) % 123457) == 0:

            print('i: ' + str(i))
            print('Credit Card Num:' + final_num)




























# Space
