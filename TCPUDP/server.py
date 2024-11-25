from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",9000))
s.listen(5)
print("............server side........")
c,a=s.accept()
while True:
    data=c.recv(1024).decode()
    print(data)
    c.send(data.encode())