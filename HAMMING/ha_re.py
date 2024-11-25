import socket

def receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 8080))
    print("Waiting for data...")

    while True:
        encoded_data, _ = sock.recvfrom(1024)
        encoded_data = encoded_data.decode()
        print(f"Received Encoded Data: {encoded_data}")

if __name__ == "__main__":
    receiver()
