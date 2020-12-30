""" 
Given two binary strings a and b, return their sum as a binary string.

 """

def addbinary(a, b):
    return "{0:b}".format(int(a, 2) + int(b, 2))


print(addbinary('1010', '1011'))