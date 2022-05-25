"""
Find secret byte
"""

hexPuzzle = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
bytePuzzle = bytes.fromhex(hexPuzzle)

""" Brute force xor bytePuzzle against the first 127 ascii codes """
for b in range(127):
    decode = ""
    for bb in bytePuzzle:
        decode += chr(b ^ bb)
    print(decode)

decode = ""
for b in bytePuzzle:
    decode += chr(b ^ 16)
print(decode)
