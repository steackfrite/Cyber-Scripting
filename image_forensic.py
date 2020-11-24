#!/bin/python3

## Import ##
# Official
from PIL import Image

def display_image(image_path):
    #Open image using Image module
    im = Image.open(image_path)
    #Show actual Image
    im.show()
    #Show rotated Image
    im = im.rotate(45)
    im.show()

    return 0

def inspect_image(image_path):
    ## Variables
    img = Image.open(image_path)

    # Image type
    img_type = img.format
    # Image mode
    img_mode = img.mode
    # Image dimension
    img_size = img.size
    # Image infos
    img_info = img.info
    # Image palette
    img_palette = img.palette

    print('Image type: ')
    print(img_type)
    print('Image mode: ')
    print(img_mode)
    print('Image size:')
    print(img_size)
    print(img_info)
    print(img_palette)

    return 0

def print_rgb(image_path):
    ## Variables
    decimal_list = ''
    bin_str = ''
    img = Image.open(image_path)
    pix = img.load()

    # start: x = 26, end: 973
    # start: y = 28 end: 1302
    # for y in range(26, 1302):
    for x in range(26, 973):
        # If Green and Blue are the same --> 1 else --> 0
        if pix[x,28][1] == pix[x, 28][2]:
            bin_str += '1'
        else:
            bin_str += '0'
            # print(pix[x,26])
            # decimal_list += str(pix[x,26][2])

    print(bin_str)

    return 0

### Main ###
if __name__ == '__main__':
    ## Variables
    image_file = '../Forensic/Stenography/Boris-Ivanov-01/Boris_Ivanov_1.jpg'
    # image_file = '../Forensic/Stenography/Exclusive-Santa/1.png'

    # inspect_image(image_file)
    print_rgb(image_file)




















# Space
