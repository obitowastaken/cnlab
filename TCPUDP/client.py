from socket import *
s=socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",9000))
print("...........client side........")
while True:
    op=input("Enter msg to send:")
    s.send(op.encode())
    data=s.recv(1024).decode()
    print(data)
 