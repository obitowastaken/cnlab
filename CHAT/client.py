from socket import *
s=socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",7000))
while True:
    msg=input("send:")
    s.send(msg.encode())
    data=s.recv(1024).decode()
    print(data)
