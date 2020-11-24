#!/bin/python3

## Import ##
# Official
import base64
import sys
# Perso
sys.path.append('/home/the-freeman/Scripts/Reco')
sys.path.append('/home/the-freeman/Scripts/')
from File import file_library as file_lib
from Manip_Data import manip_data_lib as mdata_lib

#################################################################################
#                                                                               #
# Function: Performs an incremental brutefoce XOR operation                     #
# Argument: - Cipher (String)                                                   #
# Return: Returns rows of the CSV                                               #
#                                                                               #
#################################################################################
def incremental_XOR(cipher_text):
    # Perform a XOR from 0 to 255
    for k in range(100):
        print(k, ": ", ''.join([chr(ord(c) ^ k) for c in cipher_text]))

    return 0

#################################################################################
#                                                                               #
# Function: Performs a XOR operation on two byte strings                        #
# Argument: - Base64 cipher (String)                                            #
#           - Plaintext key (String)                                            #
# Return: Returns rows of the CSV                                               #
#                                                                               #
##################################
###############################################
def base64_byte_xor(base64_ciphertext, plaintext_key):
    # Convert base64 cipher in bytes
    ba1 = base64.b64decode(base64_ciphertext)
    # Convert plaintext key in bytes
    if isinstance(plaintext_key, int):
        ba2 = bytes(plaintext_key)
    elif isinstance(plaintext_key, str):
        ba2 = plaintext_key.encode()
        ba2 = base64.b64decode(plaintext_key)

    # XOR two byte strings
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])
    # return 0

def text_byte_xor(ciphertext, plaintext_key):
    # Convert text cipher to bytes
    ba2 = []
    ba1 = ciphertext.encode()

    # Convert plaintext key in bytes
    if isinstance(plaintext_key, int):
        ba2_init = bytes([plaintext_key])
    elif isinstance(plaintext_key, str):
        ba2_init = plaintext_key.encode()

    # Building a key with the same size as the cipher
    for i in range(len(ba1)):
        ba2 += ba2_init

    # XOR two byte strings
    xor_byte = bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])
    xor_string = mdata_lib.sanitize_byte(xor_byte)
    xor_string = ''.join(xor_string)

    return xor_string

def hex_byte_xor(hex_cipher, plaintext_key):
    ## Variables
    xor_string = []
    ba2 = []

    # Convert hex string cipher to bytes
    ba1 = bytes.fromhex(hex_cipher)

    # Convert plaintext key in bytes
    if isinstance(plaintext_key, int):
        ba2_init = bytes([plaintext_key])
        # print([plaintext_key])
        # print(ba2)
    elif isinstance(plaintext_key, str):
        ba2_init = plaintext_key.encode()

    for i in range(len(ba1)):
        ba2 += ba2_init

    # XOR
    xor_bytes = bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

    # print(xor_bytes)
    xor_string = mdata_lib.sanitize_byte(xor_bytes)

    xor_string = ''.join(xor_string)
    # print(xor_string)
        # try:
        #     xor_char = byte.decode('utf-8')
        # except UnicodeDecodeError as unicode_error:
        #     xor_char = '.'
        #
        # xor_string.append(xor_char)

    return xor_string


### Main ###
if __name__ == '__main__':
    ## Variables
    # ciph = 'Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo='
    # cipher = '54454545c8504d54454552454f4941454d4d4d5645'
    cipher = '9a6b5a487840b0af692cc7a9c850e5dfb5135d04f408c96d664efee0a69ad6cbe8e6fa9be89b9ccd4a901852588b2718'
    base64_ciphertext = 'h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU'
    plaintext_key = 'Gandalf'
    base64_list = ['xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p', 'h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU', 'h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU']

    # for base64_ciph1 in base64_list:
    #     for base64_ciph2 in base64_list:
    #         key = byte_xor(base64_ciph1, base64_ciph2)
    #         print(key)

    # incremental_XOR('10001000100111111000110110100111101011101010101010111001101001011011000010011110101010011011111010100101101111111011111010010100101110011111101110101000101000001111111010110110')

    # Decode the cipher-text to a byte string and make the plaintext a byte string
    # for index_key in range(1, 256):
    #     key = hex_byte_xor(cipher, index_key)
    #
    #     print(str(index_key) + ': ' + key)

    print(text_byte_xor('B/<V5;)j}j6\\<Y)8><\\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf=', 126))


























# space
