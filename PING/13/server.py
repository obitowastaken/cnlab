from socket import *
host="127.0.0.1"
port=8000
s=socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))
print(f"UDP server running on {host}:{port}")
while True:
    c,a=s.recvfrom(1024)
    print(f"receiver from {a}:{c.decode()}")
    s.sendto(b'pong', a)