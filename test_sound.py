import socket

LAPTOP_IP = "172.17.10.154" 
LAPTOP_PORT = 50007

def play_sound_on_laptop(sound_name: str):
    try:
        with socket.create_connection((LAPTOP_IP, LAPTOP_PORT), timeout=1) as sock:
            sock.sendall(sound_name.encode("utf-8"))
            response = sock.recv(1024).decode("utf-8")
            print("Laptop audio response:", response)
    except Exception as e:
        print("Could not trigger laptop sound:", e)

if __name__ == "__main__":
    play_sound_on_laptop("hit")  # test unknown sound case