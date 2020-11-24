#!/bin/python3
### Import  ###
# Official
import sys
# Perso
sys.path.append('/home/the-freeman/Scripts/Manip_Data')
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib
import manip_data_lib as data_lib

def rot47(encoded_str, index_rot):
    decoded_str = []
    for i in range(len(encoded_str)):
        j = ord(encoded_str[i])
        # print(j)
        if j >= 33 and j <= 126:
            decoded_str.append(chr(33 + ((j + index_rot) % 94)))
        else:
            decoded_str.append(encoded_str[i])
    return ''.join(decoded_str)

def rot13(data_string):
    data_result = ""

    # Loop over characters.
    for char in data_string:
        # Convert to number with ord.
        decim = ord(char)

        # Shift number back or forward for lower case
        if decim >= ord('a') and decim <= ord('z'):
            if decim > ord('m'):
                decim -= 13
            else:
                decim += 13
        # Shift number back or forward for upper case
        elif decim >= ord('A') and decim <= ord('Z'):
            if decim > ord('M'):
                decim -= 13
            else:
                decim += 13

        # Append to result.
        data_result += chr(decim)

    # Return transformation.
    return data_result


### Main ###
if __name__ == '__main__':
    ## Variables
    # File
    data_file = '../Forensic/Stenography/HailCaesar/base64.txt'
    data_string = 'Hello World'
    # Data
    bs64_msg = 'TTFOSTBOU19BUkVfQzAwTA=='
    msg_list = []

    # data_list = file_lib.read_file(data_file)
    # with open(data_file, 'r') as d_file:
    #     data_list = d_file.read()

    # print(data_list)

    print(rot13(data_string))

    # for bs64_msg in data_list:
    #     msg = data_lib.decode_base64(bs64_msg)
    #     msg_list.append(msg)
    #
    #     print(msg)

    # print(rot47(msg, 14))
    # for i in range(47):
    #     print(rot47('b"Iqsi88E0b/Ie>=`jmcj\\x7fd2y5Eab5:aZy5Cq1dqrqFU\\x80nlHls9;).0F"', i))
