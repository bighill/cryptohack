# Notes

All notes are related to python 3

## Example data comparison

```
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
```

## chr()

Convert an ASCII ordinal number to a character.

## ord()

Convert a character to an ASCII ordinal number.

## bytes.fromhex()

Convert hex to bytes.

## bytes.hex()

Convert byte strings to hex.

## base64.b64encode()

Encode bytes into Base64.

Import base64 in order to use this: `import base64`

## PyCryptodome

The PyCryptodome library needs to be installed as a requirement. Also needs to be imported like this...

```python
from Crypto.Util.number import long_to_bytes
# or
from Crypto.Util.number import *
```

`Crypto.Util.number.long_to_bytes()` : Convert a positive integer to a byte string

`Crypto.Util.number.bytes_to_long` : Convert a byte string to a long integer

## XOR

XOR operator is denoted by a caret `^` (but sometimes ⊕)

Bit comparison: `0110 ^ 1010 = 1100`
