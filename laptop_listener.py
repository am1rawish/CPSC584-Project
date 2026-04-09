import socketserver
import pygame

LAPTOP_PORT = 50007

pygame.mixer.init()

# load sounds you want to play on the LAPTOP
SOUNDS = {
    "hit": pygame.mixer.Sound("audio/Kyoto.mp3"),
    "timer": pygame.mixer.Sound("audio/timer.mp3"),
    "lion": pygame.mixer.Sound("audio/lion.mov"),
    "croc": pygame.mixer.Sound("audio/croc.mov"),
    "gunshots": pygame.mixer.Sound("audio/gunshots.mov"),
    "lose life": pygame.mixer.Sound("audio/lose_life.mp3"),
    "game_over": pygame.mixer.Sound("audio/game_over.mp3"),

}

class AudioHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).decode("utf-8").strip()
        print(f"received: {data}")

        if data in SOUNDS:
            sound = SOUNDS[data].play()
            sound.play(maxtime=10000)   # milliseconds
            self.request.sendall(b"OK")
        else:
            self.request.sendall(b"UNKNOWN_SOUND")

if __name__ == "__main__":
    host = "0.0.0.0"   # listen on your laptop's network interface
    with socketserver.TCPServer((host, LAPTOP_PORT), AudioHandler) as server:
        print(f"Listening for sound requests on port {LAPTOP_PORT}...")
        server.serve_forever()