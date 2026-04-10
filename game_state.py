from picrawler import Picrawler
from enum import Enum, auto
import ColorDetection2 
import return_to_white_box
import read_cards
from time import sleep
import preset_actions
import send_sound
from vilib import Vilib
from robot_instance import Bala7a


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

map_pieces = []

MAX_SECTORS = 3

ROUND_DANGERS = {
    1: "lion",
    2: "gunshots",
    3: "crocodile"
}

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
    current_sector = 1

    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)
    lives = 3

    while True:

        if current_state == State.START:
            print("Welcome to the game! Starting in Sector 1.")
            preset_actions.wave_hand(Bala7a)
            send_sound.play("game_intro")
            sleep(28)

            current_state = State.ANSWERING_QUESTION

        elif current_state == State.ANSWERING_QUESTION:
            # Simulate answering a question
            print("state: ANSWERING_QUESTION")
            send_sound.play("have_1_min")
            sleep(5)
            print("You have 60 seconds to answer the question...")
            send_sound.play("timer")
            sleep(35)  # Simulate time taken to answer the question
            send_sound.play("10_s_left")
            sleep(10)
            # play music/ ticking sound 

            global init_color 
            init_color= ColorDetection2.get_initial_color()

            if init_color is None:
                print("No answer detected! You lose a life.")
                send_sound.play("lose life")
                preset_actions.look_down(Bala7a)
                preset_actions.sit(Bala7a)
                lives -= 1

                if not any_lives_remaining(lives):                               # check if we have any remaining lives          
                        current_state = State.LOSE_GAME

                elif lives == 2:
                    send_sound.play("2_lives")
                else:
                    send_sound.play("1_life")

                sleep(2)
                preset_actions.stand(Bala7a)
               

                                     # if it returns false(no more lives), lose game
                
                continue
            

            else:
                current_state = State.FIND_ANSWER_BOX

        
        elif current_state == State.FIND_ANSWER_BOX:

             ColorDetection2.find_color_box(init_color)
             send_sound.play("open_chest")
             print("Found the answer box! Reading the card...")
             current_state =State.READ_ANSWER_BOX
             

        elif current_state == State.READ_ANSWER_BOX:
            sleep(10)
            is_answer_correct = read_cards.detect_color()

            if is_answer_correct:
                print("Correct answer! Moving to next sector.")
                send_sound.play("correct_answer")
                read_cards.react(is_answer_correct)
                send_sound.play("next_sector")
                sleep(2)
                current_state = State.SWITCH_QUADRANT

            else:

                print("Wrong answer! You lose a life.")

                if current_sector == 1:
                    send_sound.play("lion")
                    read_cards.react(is_answer_correct, current_sector)
                    
                elif current_sector == 2:
                    send_sound.play("gunshots")
                    read_cards.react(is_answer_correct, current_sector)
                    
                elif current_sector == 3:
                    send_sound.play("crocodile")
                    read_cards.react(is_answer_correct, current_sector)
                    
                
                
                lives -= 1
                send_sound.play("lose life")
                preset_actions.look_down(Bala7a)
                preset_actions.sit(Bala7a)

                if not any_lives_remaining(lives):
                    current_state = State.LOSE_GAME
                    continue
                elif lives == 2:
                    send_sound.play("2_lives")
                else:
                    send_sound.play("1_life")

                sleep(2)
                preset_actions.stand(Bala7a)

                
                

                current_state = State.RETURN_TO_QUESTION_BOX

        elif current_state == State.RETURN_TO_QUESTION_BOX:
            
            return_to_white_box.return_to_white_box(init_color)

            current_state = State.ANSWERING_QUESTION

        elif current_state == State.SWITCH_QUADRANT:


            current_sector += 1

            if current_sector > MAX_SECTORS:
                current_state = State.WIN_GAME
            else:
                return_to_white_box.return_to_white_box(init_color)
                Bala7a.do_step('sit', 40)
                current_state = State.ANSWERING_QUESTION
                sleep(20)

        elif current_state == State.LOSE_GAME:
            print("Game Over! You have lost all your lives.")
            send_sound.play("game_over")
            #add lose game reaction here
            break

        elif current_state == State.WIN_GAME:
            Bala7a.do_action("backward", 6, 90)
            sleep(10)
            send_sound.play("win")
            print("Congratulations! You have won the game!")
            
            preset_actions.push_up(Bala7a)
            preset_actions.push_up(Bala7a)
            preset_actions.excited(Bala7a)
            preset_actions.nod(Bala7a)
            preset_actions.nod(Bala7a)

            #add win game reaction here
            sleep(3)
            break
    
                    
def any_lives_remaining(lives):
    if lives <= 0:
        return False
    return True


        
if __name__ == "__main__":
    main()