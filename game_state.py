from enum import Enum, auto
import ColorDetection 
import read_cards

class State(Enum):
    START = auto()
    QUADRANT_PLAY = auto()
    ANSWERING_QUESTION = auto()
    FIND_ANSWER_BOX = auto()
    SWITCH_QUADRANT = auto()
    LOSE_GAME = auto()
    WIN_GAME = auto()


current_sector = 1
lives = 3
map_pieces = []

MAX_SECTORS = 3

SECTORS = {
    1: {
        "name": "Sector 1",
        "paths": ["purple", "orange", "yellow"],
        "map_piece": "map_piece_1"
    },
    2: {
        "name": "Sector 2",
        "paths": ["purple", "orange", "yellow"],
        "map_piece": "map_piece_2"
    },
    3: {
        "name": "Sector 3",
        "paths": ["purple", "orange", "yellow"],
        "map_piece": "map_piece_3"
    }
}

def main():
    current_state = State.START

    while True:
        if current_state == State.START:
            print("Welcome to the game! Starting in Sector 1.")
            current_state = State.QUADRANT_PLAY

        elif current_state == State.ANSWERING_QUESTION:
            # Simulate answering a question
            print("You have 45 seconds to answer the question..."!)
            sleep(45)  # Simulate time taken to answer the question
            # play music/ ticking sound 
            # if no answer is given, maybe we have robot randomly picks a box to move to ??
            current_state = State.FIND_ANSWER_BOX

           

        elif current_state == State.FIND_ANSWER_BOX:
             ColorDetection.main()
        
