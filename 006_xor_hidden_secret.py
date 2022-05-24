"""
Find secret byte
"""

hexPuzzle = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
bytePuzzle = bytes.fromhex(hexPuzzle)

""" Brute force xor bytePuzzle against the first 127 ascii codes """
for b in range(127):
    decode = ""
    for bb in bytePuzzle:
        decode += chr(b ^ bb)
    print(decode)
""" Examine output to see that one of them returned crypto{0x10_15_my_f4v0ur173_by7e} """
