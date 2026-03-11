from vilib import Vilib
from time import sleep
from picrawler import Picrawler

Bala7a = Picrawler()

#start camera
v = Vilib()
v.camera_start(vflip=False, hflip=False)
v.display(local=True, web=True)

colors =  ["green", "blue", "orange"]

def detect_color():

    for color in colors:

        Vilib.color_detect(color)
        sleep(0.5)

        count = Vilib.detect_obj_parameter.get('color_n', 0)

        if count > 0:
            return color

    return None

def main():

    speed = 80

    Bala7a.do_step('stand', 40)

    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    while True:

        color = detect_color()

        if color is not None:
            print("Found",color)
            break

        print("Scanning...")
        Bala7a.do_action('turn left angle',1,speed)
        sleep(3)


    Bala7a.do_action('forward',5,speed)

if __name__ == "__main__":
    main()
