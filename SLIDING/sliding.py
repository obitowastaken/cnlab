import math
import random
import time
def sender(message, window_size):
    num_frames = math.ceil(len(message) / window_size)
    sent_frame = 0 
    while sent_frame < num_frames:
        start = sent_frame * window_size
        end = min(start + window_size, len(message))
        print(f"\nSender: Sending frames from position {start + 1} to {end}")
        for i in range(start, end):
            print(f"Frame {i + 1}: '{message[i]}' sent.")
        if random.choice([True, False]): 
            print(f"Receiver: Acknowledgment received for frames from {start + 1} to {end}")
            sent_frame += 1
        else:
            print(f"Receiver: Acknowledgment NOT received for frames from {start + 1} to {end}. Resending frames.")
            time.sleep(2) 
    print("\nAll frames sent successfully.")
def receiver(message, window_size):
    pass

if __name__ == "__main__":
        message = input("Enter the message to send: ")
        window_size = int(input("Enter the window size: "))
        sender(message, window_size)
        receiver(message,window_size)

