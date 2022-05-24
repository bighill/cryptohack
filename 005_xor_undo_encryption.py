"""
Undo encryption to find FLAG

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
"""


def hex_to_byte_list(h):
    _bytes = bytes.fromhex(h)
    result = []
    for byte in _bytes:
        result.append(byte)
    return result


def xor_byte_list(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i])
    return result


def final_xor_byte_list(a, b, c, d):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i] ^ c[i] ^ d[i])
    return result


key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key1key2 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2key3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag123 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key1ByteList = hex_to_byte_list(key1)
key2key1ByteList = hex_to_byte_list(key1key2)
key2key3ByteList = hex_to_byte_list(key2key3)
flag123ByteList = hex_to_byte_list(flag123)

key2ByteList = xor_byte_list(key1ByteList, key2key1ByteList)
key3ByteList = xor_byte_list(key2ByteList, key2key3ByteList)
flagByteList = final_xor_byte_list(
    flag123ByteList, key1ByteList, key2ByteList, key3ByteList)

flag = ""
for b in flagByteList:
    flag += chr(b)

print(flag)
