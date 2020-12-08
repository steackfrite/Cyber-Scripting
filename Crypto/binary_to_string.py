#!/usr/bin/python
## Import ##
import binascii
import sys
# Perso
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib

#################################################################################
#                                                                               #
# Function: Converts a binary string into it's ascii representation             #
# Argument: - Binary string (String)                                            #
# Return: Ascii string (String)                                                 #
#                                                                               #
#################################################################################
def binary_to_string(bin_str):
    ## Variables
    bin_decoded = ''.join(chr(int(bin_str[i*8:i*8+8],2)) for i in range(len(s)//8))

    return bin_decoded

def binary_to_string2(bin_file, result_file):
    with open(bin_file, "rb") as b_file:
        data = bytearray(b_file.read())

    data = data.replace(b'\xe2\x80\x8f', b'1')
    data = data.replace(b'\x20', b'0')
    print(data)

        # Find start of png byte
        # print(data.find(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a', 1))
        # Find end of png byte
        # print(data.find(b'\x49\x45\x4e\x44', 1))

        # data = data.replace(b'\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\x89', b'\x89')
        # data = data.decode("ascii")
        # print unbits(data)
        # print(data)
    with open(result_file, 'wb') as b_res_file:
        b_res_file.write(data)

def binary_to_string3(bin_file):
    with open(bin_file, "rb") as b_file:
        file_content = b_file.read()
        print(file_content)

    # First we must split the string into a list so we can get bytes easier.
    bin_list = []
    for i in range(0, len(file_content), 8): # 8 bits in a byte!
        bin_list.append(file_content[i:i+8])

    # for i in range((len(bin_list) - 220696), len(bin_list)):
    # for i in range((len(bin_list) - 52398), len(bin_list)):
    # print(bin_list[len(bin_list) - 220696])
    # print(len(bin_list))
    # print(bin_list)

    # message = ''
    # for binary_value in bin_list:
    #     binary_integer = int(binary_value, 2) # Convert the binary value to base2
    #     ascii_character = chr(binary_integer) # Convert integer to ascii value
    #
    #     message+=ascii_character

    # print(bin_list)


### Main ###
if __name__ == '__main__':
    ## Variables
    bin_list = []
    bin_file = '/home/the-freeman/Security/Challenges/CTFlearn/Forensic/Stenography/Blank-Page/TheMessage.txt'
    # bin_file = '/home/the-freeman/Security/Challenges/CTFlearn/Forensic/Stenography/The-Keymaker/flag.enc'
    result_file = '/home/the-freeman/Security/Challenges/CTFlearn/Forensic/Stenography/Blank-Page/test.txt'

    binary_to_string2(bin_file, result_file)
    # binary_to_string3(bin_file)

    # with open(bin_file, 'rb') as file:
    #     file_content = file.read().hex()
    #     file_content = file_content.replace('20', '0').replace('80', '1').replace('e2', '1').replace('8f', '1')
        # file_content = file_content.replace('20', '1').replace('80', '0').replace('e2', '0').replace('8f', '0')

    # print(file_content)

    # with open(bin_file, 'wb') as b_file:
    #     b_data = b'\x43\x6d\x6d\x74\x61\x53\x48\x68\x41\x73\x4b\x39\x70\x4c\x4d\x65\x70\x79\x46\x44\x6c\x33\x37\x55\x54\x58\x51\x54\x30\x43\x4d\x6c\x74\x5a\x6b\x37\x2b\x34\x4b\x61\x61\x31\x73\x76\x6f\x35\x76\x71\x62\x36\x4a\x75\x63\x7a\x55\x71\x51\x47\x46\x4a\x59\x69\x79\x63\x59'
    #
    #     b_file.write(b_data)



























# Space
