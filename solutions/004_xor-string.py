# from pwn import *
# res = xor("label", 13)

def xor_string_13(string):
    """ convert each char to ascii, xor that against 13, then convert result ascii back to string """
    res = ""

    for char in string:
        """ ord() converts character to ascii """
        x = ord(char) ^ 13
        """ chr() converts ascii to character string """
        res += chr(x)

    return res


s = xor_string_13('label')
print(s)
