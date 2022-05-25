from Crypto.Util.number import *

base10 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

""" Convert long to byte string """
bytes = long_to_bytes(base10)

print(bytes)
