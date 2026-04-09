from vilib import Vilib
from time import sleep
from picrawler import Picrawler
from twist import twist
#import preset_actions
import sys
import os

sys.path.append(os.path.expanduser("~/picrawler/examples"))

import preset_actions

# read cards in treasure/danger boxes
# if card is blue --> answer is correct --> go to next area
# if card is red --> answer is wrong --> return back to question box

Bala7a = Picrawler()

def detect_color():

    colors =  ["red", "blue"]

    while True:
        for color in colors:

            Vilib.color_detect(color)
            sleep(3)

            count = Vilib.detect_obj_parameter.get('color_n', 0)

            if count > 0:
                if color == "red":
                    answer = False
                    break

                if color == "blue":
                    answer = True
                    break
            else:
                print(f"No card detected, scanning again...")
                continue 

    return answer

def react(answer_value):

    if answer_value == False:
        print("reacting to wrong answer")
        preset_actions.shake_head()
        preset_action.look_up()
        preset_actions.fighting()
        # sounds here
        #movements here
       

    elif answer_value == True:
        #movements here
        i = 0
        while i <= 10:
            twist(speed=100)
            i += 1

        # maybe add audio if speaker issue gets fixed
       


def main():
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    try:
        while True:
            color = detect_color()

            if color is None:
                print("No card detected, scanning")
                continue
            else:
                react(color)
                break

        return True if color=="blue" else False

    except KeyboardInterrupt:
        print("\nCtrl+C detected, exiting safely...")


def test():
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    detected_color = detect_color()
    react(detected_color)

if __name__ == "__main__":
    test()