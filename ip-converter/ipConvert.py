#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~

import math
from sys import argv

file = open(argv[1], "r") #This will let me specify a file argument when run to parse through

# Functions for conversions
def vert(ip): #The god damn << indicates a bitwise shift left. If you only put one it will only convert one god damn octet!!
    ver = '.'.join([str(int(ip) >> (i << 3) & 0xFF)
            for i in range(4)[::-1]])
    return str(ver)
 
def dQuad(ip): #convert dotted quad ips to decimal format
    try:
        x = ip.split('.')
        math = int(x[0]) * 256**3 + int(x[1]) * 256**2 + int(x[2]) * 256 + int(x[3])
        return str(math) #testing the removal of return math to see
    except:
        return None

def dec2ip(ip):
    try:
        if int(ip) < 0:
            return("Number is not a valid IPv4 Address, its less than 0.0.0.0")
        elif int(ip) > 4294967295:
            return("Number is not a valid IPv4 Address, it is greater than 255.255.255.255")
        else:
            y = vert(ip)
            return str(y) #changed from return to print for testing
    except:
        return None

def dataCheck(file):
    try:
        for ip in file:
            ip = ip.strip("\n")
            out = dQuad(ip)
            if out is None:
                out = dec2ip(ip)
                if out is None:
                    print("Nothing Worked! ¯\_(ツ)_/¯ - Invalid Input (1 octet > 255 or ASCII data present)")
                else:
                    print out
            else:
                if int(out) > 4294967295:
                    print("Number is not a valid IPv4 Address, it is greater than 255.255.255.255")
                else:
                    print out
    except Exception as e:
        print("Error with Data", e)

banner = "\n[+] Converted IP Addresses [+]\n+--------------------------------+"

print banner
dataCheck(file)
