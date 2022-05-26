# from pwn import *
# res = xor("label", 13)
""" pwn.xor() can accomplish the goal easily. Below is the hard way. """

def do_the_xor(string, n):
    """ convert each char to ascii, xor that against 13, then convert result ascii back to string """
    res = ""

    for char in string:
        """ ord() converts character to ascii """
        x = ord(char) ^ n
        """ chr() converts ascii to character string """
        res += chr(x)

    return res


s = do_the_xor('label', 13)
print(s)
