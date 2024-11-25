import socket

def calculate_parity(bits, positions):
    count = sum(bits[pos - 1] for pos in positions)
    return count % 2

def hamming_encode(data):
    data_bits = list(map(int, data))
    encoded = [0] * 7
    encoded[2] = data_bits[0]
    encoded[4] = data_bits[1]
    encoded[5] = data_bits[2]
    encoded[6] = data_bits[3]
    encoded[0] = calculate_parity(encoded, [1, 3, 5, 7])
    encoded[1] = calculate_parity(encoded, [2, 3, 6, 7])
    encoded[3] = calculate_parity(encoded, [4, 5, 6, 7])
    return ''.join(map(str, encoded))

def sender():
    input_bits = input("Enter 4-bit data stream: ")
    if len(input_bits) != 4 or not set(input_bits).issubset({'0', '1'}):
        print("Invalid input. Please enter exactly 4 bits (0s and 1s).")
        return

    encoded_data = hamming_encode(input_bits)
    print("Encoded Hamming code:", encoded_data)

    # Sending data over UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(encoded_data.encode(), ("127.0.0.1", 8080))
    print("Data sent.")

# Run the sender function
sender()
