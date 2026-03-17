from vilib import Vilib
from time import sleep
from picrawler import Picrawler

Bala7a = Picrawler()

colors =  ["green", "blue", "orange"]

def detect_color():

    for color in colors:

        Vilib.color_detect(color)
        sleep(2)

        count = Vilib.detect_obj_parameter.get('color_n', 0)

        if count > 0:
            return color

    return None

def align_to_color(color):

    is_aligned = False

    Vilib.color_detect(color)

    while True:

        count = Vilib.detect_obj_parameter.get('color_n',0)
        

        if count == 0:
            print("Lost color")
            is_aligned = False
            return is_aligned

        x = Vilib.detect_obj_parameter.get('color_x')
        w = Vilib.detect_obj_parameter.get('color_w')

        print("Color position start:", x)
        print("Color distance start:", w)

        if x < 250:
            Bala7a.do_action('turn left angle',1,80)
            print("Color position l:", x)

        if x > 400:
            Bala7a.do_action('turn right angle',1,80)
            print("Color position right:", x)

        if w < 65:
            Bala7a.do_action('turn left', 1, 80)
            Bala7a.do_action('forward', 1, 80)
            print("Color distance f:", w)
        
        if w > 85:
            Bala7a.do_action('backward', 1, 80)
            print("Color distance b:", w)

        elif 200 <= x <= 400 and 65 <= w <= 85:
            print("Final distance:", w)
            print("Final position:", x)
            is_aligned = True
            print("Aligned with color!")
            return False

        else:
            return

    return is_aligned


def main():

    speed = 80

    Bala7a.do_step('stand', 40)

    # Start camera and display
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    sleep(1)

    while True:

        color = detect_color()

        if color is None:
            print("No color detected, scanning...")
            Bala7a.do_action('turn left',1,speed)

        else: 
            print(f"Detected color: {color}")
            
            aligned = align_to_color(color)

            if not aligned:
              print("Failed to align with color, scanning again...")

            else:
                print("Successfully aligned with color!")
                break

if __name__ == "__main__":
    main()
