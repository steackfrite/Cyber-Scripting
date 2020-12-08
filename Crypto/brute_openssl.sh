#!/bin/bash
## Variables
list_hex='0123456789abcdef'
# list_hex='01'
SOF0='0800be00c803011100021101031101'
SOS='000C03010002110311003F0000F9766BFC44BEDA8F3F5C031B92CB0E92D6BDC9'
flag_file='../../Security/Challenges/CTFlearn/Forensic/Stenography/The-Keymaker/flag.enc'
flag_file_res='../../Security/Challenges/CTFlearn/Forensic/Stenography/The-Keymaker/Test/flag'

for (( i=0; i<${#list_hex}; i++ ));
do
  for (( j=0; j<${#list_hex}; j++ ));
  do
    SOF0_final=$SOF0${list_hex:$i:1}${list_hex:$j:1}
    flag_file_final=$flag_file_res${list_hex:$i:1}${list_hex:$j:1}
    # echo $SOF0_final
    echo "${list_hex:$i:1}""${list_hex:$j:1}"
    openssl enc -d -aes-256-cbc -iv $SOF0_final -K $SOS -in $flag_file -out $flag_file_final -base64
  done
done
