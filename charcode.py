#!/usr/bin/python


# Replace the array with the char codes from the attacker webpage
# and update the value in the X equation with the value being subtracted in the code (in this instance it is 97)

# From what I have observed, the attackers using this method do not reuse the same value. 


array = [201,213,213,209,155,144,144,195,214,211,207,202,207,200,149,199,194,213,212,143,216,208,211,205,197,144,160,194,158,146,204,200,164,135,196,158,197,202,198,213]
finalSTR = []

for x in array:
    x = x - 97
    finalSTR.append(chr(x))

print(''.join(finalSTR))
