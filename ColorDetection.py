from vilib import Vilib
from time import sleep
from picrawler import Picrawler

Bala7a = Picrawler()

move_history = []

colors =  ["purple", "orange", "yellow"] # color of answer boxes

def move(action, duration, speed=40):
    Bala7a.do_action(action, duration, speed)

    # Store the action in the move history
    move_history.append((action, duration, speed))

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

    while True:
        Vilib.color_detect(color)
        count = Vilib.detect_obj_parameter.get('color_n',0)
        

        if count == 0:
            print("Lost color")
            is_aligned = False
            break

        x = Vilib.detect_obj_parameter.get('color_x')
        w = Vilib.detect_obj_parameter.get('color_w')

        print("Color position start:", x)
        # print("Color distance start:", w)

        if x < 250:
            move('turn left angle',1,35)
            print("Color position l:", x)
      

        elif x > 400:
            move('turn right angle',1,35)
            print("Color position right:", x)

        elif w < 140:
            move('forward', 1, 65)
            print("Color distance f:", w)
        
        elif w > 380:
            move('backward', 1, 65)
            print("Color distance b:", w)

        else:
            print("Final position:", x)
            print("Final distance:", w)
            is_aligned = True
            print("Aligned with color!")
            Bala7a.do_step('sit', 40)
            break

    return is_aligned
    
        


def main():

    speed = 60

    Bala7a.do_step('stand', 40)

    # Start camera and display
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    sleep(1)

    init_color = detect_color()
    print(f"Initial detected color: {init_color}")
    move('turn left',1,speed)
    while True:
        try:
            move('turn left',1,speed)
            color = Vilib.color_detect(init_color)
            n = Vilib.detect_obj_parameter['color_n']
            sleep(2)
            print("n: ", n)
            
            if n < 1:                
                print("No color detected, scanning...")
                continue

            else:
                print(f"Detected color: {color} (test w purple)")
                aligned = align_to_color('purple')

                if not aligned:
                    print("Failed to align with color, scanning again...")

                else:
                    print("Successfully aligned with color!")
                    break

        except KeyboardInterrupt:
            print("\nCtrl+C pressed...")
        finally:
            Bala7a.do_step('sit', 40)

if __name__ == "__main__":
    main()
