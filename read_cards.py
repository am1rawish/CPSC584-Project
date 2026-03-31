from vilib import Vilib
from time import sleep
from picrawler import Picrawler
from twist import twist

# read cards in treasure/danger boxes
# if card is blue --> answer is correct --> go to next area
# if card is red --> answer is wrong --> return back to question box

Bala7a = Picrawler()

def detect_color():

    colors =  ["red", "blue"]

    for color in colors:

        Vilib.color_detect(color)
        sleep(2)

        count = Vilib.detect_obj_parameter.get('color_n', 0)

        if count > 0:
            return color

    return None

def react(detected_color):

    if detected_color == "red":
        print("reacting to wrong answer")
        #movements here
       

    elif detected_color == "blue":
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
                print("No card detected")
                continue
            else:
                react(color)
                break

        return color

    except KeyboardInterrupt:
        print("\nCtrl+C detected, exiting safely...")

if __name__ == "__main__":
    main()