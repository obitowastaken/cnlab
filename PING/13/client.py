from socket import *
import time
host="127.0.0.1"
port=8000
s=socket(AF_INET,SOCK_DGRAM)
s.settimeout(2)
start=time.time()
s.sendto(b'ping',(host,port))
c,a=s.recvfrom(1024)
end=time.time()
print(f"received {c.decode()} from {a} in {end-start:.2f} seconds")

    