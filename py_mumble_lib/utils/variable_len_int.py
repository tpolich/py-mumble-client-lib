__author__ = 'Tim'

#specification https://github.com/mumble-voip/mumble/raw/master/doc/mumble-protocol.pdf
#section 5.4 "varint, 64-bit interger encoding"


from struct import *

def __test():
    for x in range(-3, 1):
        if decode(encode(x)) != x:
            raise RuntimeError("FAILED FOR VALUE " + str(x))
    i = 1
    while i < pow(2, 63) - 1:
        if decode(encode(i)) != i:
            raise RuntimeError("FAILED FOR VALUE " + str(i))
        if decode(encode(i * -1)) != i * -1:
            raise RuntimeError("FAILED FOR VALUE " + str(i * -1))
        i <<= 1


def encode(number):

    if number < 0:
        if number >= -3:
            return pack("!B", 0xfc | (number * -1))
        else:
            return pack("!B", 0xf8) + encode(number * -1)

    if number < 0x80:
        return pack("!B", number)
    if number < 0x4000:
        return pack("!H", number | 0x8000)
    if number < 0x200000:
        return pack("!BH", 0xc0 | (number >> 16), number & 0xffff)
    if number < 0x10000000:
        return pack("!L", 0xe0000000 | number)
    if number < 0x100000000:
        return pack("!BL", 0xf0, number)

    return pack("!BQ", 0xf4, number)


def decode(binary_string):
    if len(binary_string) < 1:
        raise "Data Length can't be 0"

    (byte_one, ) = unpack("!B", binary_string[0])
    if byte_one & 0x80 == 0x0:
        return byte_one & 0x7f
    if byte_one & 0xc0 == 0x80:
        return ((byte_one & 0x3f) << 8) + unpack("!B", binary_string[1])[0]
    if byte_one & 0xe0 == 0xc0:
        return ((byte_one & 0x1f) << 16) + unpack("!H", binary_string[1:3])[0]
    if byte_one & 0xf0 == 0xe0:
        return unpack("!L", binary_string[:4])[0] & 0x0fffffff

    first_six = byte_one & 0xfc

    if first_six == 0xf0:
        return unpack("!L", binary_string[1:5])[0]
    if first_six == 0xf4:
        return unpack("!Q", binary_string[1:9])[0]
    if first_six == 0xf8:
        return decode(binary_string[1:]) * -1
    if first_six == 0xfc:
        return (unpack("!B", binary_string[0])[0] & 0x3) * -1

    raise "Not a variable length int"