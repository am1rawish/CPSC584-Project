from vilib import Vilib
from time import sleep
from picrawler import Picrawler

Bala7a = Picrawler()

colors =  ["green", "blue", "orange", "yellow"]

def detect_color():

    for color in colors:

        Vilib.color_detect(color)
        sleep(2)

        count = Vilib.detect_obj_parameter.get('color_n', 0)

        if count > 0:
            return color

    return None

def align_to_color(color):
    Vilib.color_detect(color)
    sleep(0.5)

    is_aligned = False
    speeed = 40

    
    
    while True:
        count = Vilib.detect_obj_parameter.get('color_n',0)
        

        if count == 0:
            print("Lost color")
            is_aligned = False
            return False

        x = Vilib.detect_obj_parameter.get('color_x')

        if x is None:
            print("No x value yet")
            sleep(0.2)
            continue

        
        #w = Vilib.detect_obj_parameter.get('color_w')

        print("Color position start:", x)
        # print("Color distance start:", w)

        if x < 250:
            print("Too far left -> turning left a little")
            Bala7a.do_action('turn left angle',1,35)
            sleep(0.5)

            new_x = Vilib.detect_obj_parameter.get('color_x')
            print("Updated x after left turn:", new_x)
      

        elif x > 400:
            print("Too far right -> turning right a little")
            Bala7a.do_action('turn right angle',1,35)
            sleep(0.5)
            new_x = Vilib.detect_obj_parameter.get('color_x')
            print("Updated x after right turn:", new_x)

        else:
            print("Final position:", x)
            is_aligned = True
            print("Aligned with color!")
            Bala7a.do_step('sit', 40)
            break

    return is_aligned
    """
        if w < 130:
            Bala7a.do_action('forward', 1, 60)
            print("Color distance f:", w)
        
        if w > 300:
            Bala7a.do_action('backward', 1, 60)
            print("Color distance b:", w)
"""
"""
        elif 200 <= x <= 400 and 65 <= w <= 85:
            print("Final distance:", w)
            print("Final position:", x)
            is_aligned = True
            print("Aligned with color!")
            return False
"""


def main():

    speed = 60

    Bala7a.do_step('stand', 40)

    # Start camera and display
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    sleep(1)

    init_color = detect_color()
    print(f"Initial detected color: {init_color}")
    Bala7a.do_action('turn left',1,speed)
    while True:

        Bala7a.do_action('turn left',1,speed)
        Vilib.color_detect(init_color)
        sleep(2)
        n = Vilib.detect_obj_parameter['color_n']
        
        print("n: ", n)
        
        if n < 1:                
            print("No color detected, scanning...")
            continue

        else:
            print(f"Detected color: {init_color}")
            aligned = align_to_color(init_color)

            if not aligned:
              print("Failed to align with color, scanning again...")

            else:
                print("Successfully aligned with color!")
                break

if __name__ == "__main__":
    main()
