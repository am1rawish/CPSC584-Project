from enum import Enum, auto
import ColorDetection 
import read_cards
from sleep import time

class State(Enum):
    START = auto()
    QUADRANT_PLAY = auto()
    ANSWERING_QUESTION = auto()
    FIND_ANSWER_BOX = auto()
    READ_ANSWER_BOX = auto()
    RETURN_TO_QUESTION_BOX = auto()
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
            print("You have 45 seconds to answer the question...")
            sleep(45)  # Simulate time taken to answer the question
            # play music/ ticking sound 

            # if no answer is given, maybe we have robot randomly picks a box to move to ??
            init_color = ColorDetection.get_initial_color()
            if init_color is None:
                lives -= 1
                #need life lost reaction here

                if not any_lives_remaining():                            # check if we have any remaining lives
                        current_state = State.LOSE_GAME                 # if it returns false(no more lives), lose game
                
                continue
            

            else:
                current_state = State.FIND_ANSWER_BOX

        
        elif current_state == State.FIND_ANSWER_BOX:
        
           
             ColorDetection.find_color_box()
             State.READ_ANSWER_BOX
             

        elif current_state == State.READ_ANSWER_BOX:
        
            is_answer_correct = read_cards.main()

            if is_answer_correct:
                print("Correct answer! Moving to next sector.")
                current_state = State.SWITCH_QUADRANT

            else:
                print("Wrong answer! You lose a life.")
                lives -= 1
                if not any_lives_remaining():
                    current_state = State.LOSE_GAME
                    continue

                State.RETURN_TO_QUESTION_BOX

        elif current_state == State.RETURN_TO_QUESTION_BOX:
            print("Returning to question box...")
            # add movement code here to return to question box
            State.ANSWERING_QUESTION

        elif current_state == State.SWITCH_QUADRANT:
            filler_var = True

        elif current_state == State.LOSE_GAME:
            print("Game Over! You have lost all your lives.")
            #add lsoe game reaction here
            break

        elif current_state == State.WIN_GAME:
            print("Congratulations! You have won the game!")
            #add win game reaction here
            break
    
                    
def any_lives_remaining():
    if lives <= 0:
        return False
    return True
        
if __name__ == "__main__":
    main()