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
        elif j == 32:
            decoded_str.append(char(126))
        else:
            decoded_str.append(data_lib.sanitize_byte(j))
    return ''.join(decoded_str)

def rot13(data_string):
    data_result = ""
    delete_char = False

    # Loop over characters.
    for char in data_string:
        # Convert to number with ord.
        decim = ord(char)
        delete_char = False

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
        else:
            delete_char = True

        if not delete_char:
            # Append to result.
            data_result += chr(decim)

    # Return transformation.
    return data_result

def special_rot(data_string):
    data_result = ""
    delete_char = False

    # Loop over characters.
    for char in data_string:
        # Convert to number with ord.
        decim = ord(char)
        delete_char = False

        # Shift number back or forward for lower case
        if decim >= 32 and decim <= 126:
            if decim > 113:
                decim -= (32 + 13) - (126 - decim)
            else:
                decim += 13
        else:
            delete_char = True

        if not delete_char:
            # Append to result.
            data_result += chr(decim)

    # Return transformation.
    return data_result

def returned_rot(data_string):
    ## Variables
    data_result_temp = ''
    data_result = ''
    i = 1

    # Loop at least 4 times to get the whole flag
    for j in range (2):
        # Shifting i. Part of deciphering the flag
        # i = j + 1
        # print(j)
        # Special ROT (-1 then -2, etc.)
        for char in data_string:
            # print(char)
            decim = ord(char)
            # print(decim)
            diff = decim - i
            if diff <= ord('A'):
                diff_02 = ord('A') - diff
                # Convert to number with ord
                decim = ord('Z') - diff_02
                if decim == ord('E') or decim == ord('U') or decim == ord('R') or decim == ord('O'):
                    decim -= 1

            elif diff >= ord('Z') and diff <= ord('a'):
                diff_02 = ord('a') - diff
                decim = ord('}') - diff_02
                if decim == ord('e') or decim == ord('u') or decim == ord('r') or decim == ord('o'):
                    # print(decim)
                    decim -= 1
            else:
                if decim == ord('e') or decim == ord('u') or decim == ord('r') or decim == ord('o'):
                    # print(chr(decim))
                    decim = diff - 1
                    # print(chr(decim))
                elif decim == ord('E') or decim == ord('U') or decim == ord('R') or decim == ord('O'):
                    decim = diff - 1
                else:
                    print(chr(decim))
                    decim = diff
                # print(chr(decim))

            data_result_temp += chr(decim)
            i += 1
            # print(data_result_temp)
        data_string = data_result_temp
        data_result += data_result_temp
        data_result_temp = ''

    print(data_result)
    return data_result

def findflag_returned(data_string):
    ## Variables
    data_result = ''
    i = 1

    for char in data_string:
        decim = ord(char) + i
        data_result += chr(decim)
        i += 1

    print(data_result)


### Main ###
if __name__ == '__main__':
    ## Variables
    # File
    data_file = '../Forensic/Stenography/HailCaesar/base64.txt'
    data_string = 'Iqsi'
    # Data
    bs64_msg = 'TTFOSTBOU19BUkVfQzAwTA=='
    msg_list = []

    # data_list = file_lib.read_file(data_file)
    # with open(data_file, 'r') as d_file:
    #     data_list = d_file.read()

    # print(data_list)

    # print(special_rot(data_string))

    # for bs64_msg in data_list:
    #     msg = data_lib.decode_base64(bs64_msg)
    #     msg_list.append(msg)
    #
    #     print(msg)

    # returned_rot('jmcj')
    returned_rot('Iqsi')
    # findflag_returned('flag')

    # print(rot47(msg, 14))
    # for i in range(93):
    #     print(rot47('b"Iqsi88E0b/Ie>=`jmcj\\x7fd2y5Eab5:aZy5Cq1dqrqFU\\x80nlHls9;).0F"', i))
