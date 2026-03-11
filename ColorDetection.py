from vilib import Vilib
from time import sleep
from picrawler import Picrawler

Bala7a = Picrawler()

colors =  ["green", "blue", "orange"]

def detect_color():

    for color in colors:

        Vilib.color_detect(color)
        sleep(3)

        count = Vilib.detect_obj_parameter.get('color_n', 0)

        if count > 0:
            return color

    return None

def align_to_color(color):


    Vilib.color_detect(color)

    while True:

        count = Vilib.detect_obj_parameter.get('color_n',0)

        if count == 0:
            print("Lost color")
            return False

        x = Vilib.detect_obj_parameter.get('color_x')

        print("Color position:", x)

        if x < 120:
            Bala7a.do_action('turn left angle',1,80)

        elif x > 200:
            Bala7a.do_action('turn right angle',1,80)

        else:
            print("Aligned!")
            return True

        sleep(0.4)


def main():

    speed = 80

    Bala7a.do_step('stand', 40)

    # Start camera and display
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    sleep(3)

    while True:

        color = detect_color()

        if color is None:
            print("No color detected, scanning...")
            Bala7a.do_action('turn left angle',1,speed)
            sleep(3)

        else: 
            print(f"Detected color: {color}")
            
            aligned = align_to_color(color)

            if aligned:
                print(f"Moving towards {color} path")
                Bala7a.do_action('forward', 6, speed)

            break


if __name__ == "__main__":
    main()
