### Import ###
# Official
import re
import sys
# Personal
sys.path.append('/home/the-freeman/Scripts/Reco')
from File import file_library as file_lib
### Import ###

def passport_01(passport_file):
    ## Variables
    i = 0
    lines = file_lib.read_file(passport_file)
    passport = {}
    passport_list = []
    property_id = ['ecl','pid','eyr','hcl','byr','iyr','cid','hgt']
    property_list = []
    property_01 = []
    property_02 = []
    property_03 = []

    for str in lines:
        if len(str) > 0:
            # if str.find(' ') != 0:
            passport.update(dict(subString.split(':') for subString in str.split(' ')))
            # print(passport)
        else:
            # print('to be added')
            # print(passport)
            passport_list.append(passport)
            passport = {}

    for passp in passport_list:
        if 'byr' in passp and 'iyr' in passp and 'eyr' in passp and 'hgt' in passp and 'hcl' in passp and 'ecl' in passp and 'pid' in passp:

            # print(passp)
            i += 1
        # elif 'cid' not in passp:
            # print(len(passp.keys()))
            # print(passp)

    # print(len(passport_list))
    print(passport_list)
    print(i)

    return 0

def passport_02(passport_file):
    ## Variables
    i = 0
    lines = file_lib.read_file(passport_file)
    passport = {}
    passport_list = []
    property_id = ['ecl','pid','eyr','hcl','byr','iyr','cid','hgt']
    property_list = []
    property_01 = []
    property_02 = []
    property_03 = []

    for str in lines:
        if len(str) > 0:
            # if str.find(' ') != 0:
            passport.update(dict(subString.split(':') for subString in str.split(' ')))
            # print(passport)
        else:
            # print('to be added')
            # print(passport)
            passport
            passport_list.append(passport)
            passport = {}

    for passp in passport_list:
        if 'byr' in passp and 'iyr' in passp and 'eyr' in passp and 'hgt' in passp and 'hcl' in passp and 'ecl' in passp and 'pid' in passp:
            if int(passp['byr']) >= 1920 and int(passp['byr']) <= 2002 and int(passp['iyr']) >= 2010 and int(passp['iyr']) <= 2020 and int(passp['eyr']) >= 2020 and int(passp['eyr']) <= 2030 :
                regex_hgt_01 = re.search('^[0-9]{3}cm', passp['hgt'])
                regex_hgt_02 = re.search('^[0-9]{2}in', passp['hgt'])
                height_cm = re.findall('^[0-9]{3}', passp['hgt'])
                height_in = re.findall('^[0-9]{2}', passp['hgt'])
                if (regex_hgt_01 is not None and int(height_cm[0]) >= 150 and int(height_cm[0]) <= 193) or (regex_hgt_02 is not None and int(height_in[0]) >= 59 and int(height_in[0]) <= 76):
                # if (regex_hgt_01 is not None) and int(height[0]) >= 150 and int(height[0]) <= 193:
                    regex_hcl = re.search('^#([a-f]|[0-9]){6}', passp['hcl'])
                    if regex_hcl is not None:
                        regex_ecl = re.search('amb|blu|brn|gry|grn|hzl|oth', passp['ecl'])
                        if regex_ecl is not None:
                            regex_pid = re.search('[0-9]{9}', passp['pid'])
                            if regex_pid is not None:
                                i += 1
                                # print(passp['hgt'])
                                print(passp)

    # print(len(passport_list))
    # print(passport_list)
    print(i)

    return 0


### Main ###
if __name__ == '__main__':
    ## Variables
    passport_file = '/home/the-freeman/Security/Challenges/Advent-Of-Code/Chal-04/passport_list.txt'

    passport_02(passport_file)























# space
