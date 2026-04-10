import socketserver
import pygame

LAPTOP_PORT = 50007

pygame.mixer.init()

# load sounds you want to play on the LAPTOP
SOUNDS = {
    "hit": pygame.mixer.Sound("Kyoto.mp3"),
    "timer": pygame.mixer.Sound("timer.mp3"),
    "lion": pygame.mixer.Sound("lion.mp3"),
    "croc": pygame.mixer.Sound("croc.mp3"),
    "gunshots": pygame.mixer.Sound("gunshots.mp3"),
    "lose life": pygame.mixer.Sound("lose_life.mp3"),
    "game_over": pygame.mixer.Sound("game_over.mp3"),
    "game_intro": pygame.mixer.Sound("game_intro.mp3"),
    "next_sector": pygame.mixer.Sound("next_sector.mp3"),
    "open_chest": pygame.mixer.Sound("open_chest.mp3"),
    "win": pygame.mixer.Sound("win.mp3"),
    "have_1_min": pygame.mixer.Sound("have_1_min.mp3"),
    "correct_answer": pygame.mixer.Sound("correct_answer.mp3"),
    "10_s_left": pygame.mixer.Sound("10_s_left.mp3"),
    "1_life": pygame.mixer.Sound("1_life.mp3"),
    "2_lives": pygame.mixer.Sound("2_lives.mp3"),

}

class AudioHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).decode("utf-8").strip()
        print(f"received: {data}")

        if data in SOUNDS:
            sound = SOUNDS[data]
            if data == "win":
                sound.play(maxtime=14000)
            else:   
                sound.play(maxtime=50000)  # play full intro   # milliseconds
            self.request.sendall(b"OK")
        else:
            self.request.sendall(b"UNKNOWN_SOUND")

if __name__ == "__main__":
    host = "0.0.0.0"   # listen on your laptop's network interface
    with socketserver.TCPServer((host, LAPTOP_PORT), AudioHandler) as server:
        print(f"Listening for sound requests on port {LAPTOP_PORT}...")
        server.serve_forever()