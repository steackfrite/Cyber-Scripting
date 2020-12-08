#!/usr/bin/python
import base64


    ## Variables
def decode_base64(b64_msg):
    # base64_message = 'Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo='
    base64_list = ['TTFOSTBOU19BUkVfQzAwTA==']
    # base64_list = ['xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p', 'h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU']
    message_list = []

    # base64_bytes = base64_list[0].encode('ascii')
    # message_bytes = base64.b64decode(base64_bytes)
    # print(message_bytes.decode('ascii'))
    # print('Outside loop')
    # print(message_bytes)

    # Encode Strings to bytes
    bs64_bytes = b64_msg.encode('ascii')
    # Decode Base64 String bytes to ASCII String bytes
    msg_bytes = base64.b64decode(bs64_bytes)
    # Encode bytes to ASCII Strings
    msg = msg_bytes.decode('ascii')

    # Loop for decoding
    # for base64_char in base64_list:
    #     # print(base64_message)
    #     base64_bytes = base64_char.encode('ascii')
    #     message_bytes = base64.b64decode(base64_bytes)
    #     # print(message_bytes)
    #     print(message_bytes.decode('ascii'))
        # message_list.append(message_bytes.decode('ascii'))

    # print(message)

### Main ###
if __name__ == '__main__':

    decode_base64()
