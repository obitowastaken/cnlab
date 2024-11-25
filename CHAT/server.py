from socket import *
s=socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1",7000))
s.listen(5)
c,a=s.accept()
while True:
    data=c.recv(1024).decode()
    print(data)
    msg=input("send :")
    c.send(msg.encode())