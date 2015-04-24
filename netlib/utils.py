from __future__ import (absolute_import, print_function, division)


def isascii(s):
    try:
        s.decode("ascii")
    except ValueError:
        return False
    return True


# best way to do it in python 2.x
def bytes_to_int(i):
    return int(i.encode('hex'), 16)


def cleanBin(s, fixspacing=False):
    """
        Cleans binary data to make it safe to display. If fixspacing is True,
        tabs, newlines and so forth will be maintained, if not, they will be
        replaced with a placeholder.
    """
    parts = []
    for i in s:
        o = ord(i)
        if (o > 31 and o < 127):
            parts.append(i)
        elif i in "\n\t" and not fixspacing:
            parts.append(i)
        else:
            parts.append(".")
    return "".join(parts)


def hexdump(s):
    """
        Returns a set of tuples:
            (offset, hex, str)
    """
    parts = []
    for i in range(0, len(s), 16):
        o = "%.10x" % i
        part = s[i:i + 16]
        x = " ".join("%.2x" % ord(i) for i in part)
        if len(part) < 16:
            x += " "
            x += " ".join("  " for i in range(16 - len(part)))
        parts.append(
            (o, x, cleanBin(part, True))
        )
    return parts


def setbit(byte, offset, value):
    """
        Set a bit in a byte to 1 if value is truthy, 0 if not.
    """
    if value:
        return byte | (1 << offset)
    else:
        return byte & ~(1 << offset)


def getbit(byte, offset):
    mask = 1 << offset
    if byte & mask:
        return True
