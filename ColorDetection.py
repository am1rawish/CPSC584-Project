from vilib import Vilib
from time import sleep
from picrawler import Picrawler
from robot_instance import Bala7a

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
        print("Color distance start:", w)

        if x < 200:
            move('turn left angle',1,45)
            print("Color position l:", x)
            continue
      
        elif w < 420:
            move('forward', 2, 60)
            print("Color distance f:", w)
            continue
        
        elif w < 470:
            move('forward', 1, 60)
            print("Color distance f(1):", w)
            continue

        elif x > 500:
            move('turn right angle',1,45)
            print("Color position right:", x)
            continue

        else:
            print("Final position:", x)
            print("Final distance:", w)
            is_aligned = True
            print("Aligned with color!")
            Bala7a.do_step('sit', 40)
            break

    return is_aligned


def get_initial_color():
    init_color = detect_color()
    sleep(1)
    """
    while init_color is None:
        print("No color detected, looking")
        init_color = detect_color()
    """  
    print(f"Initial detected color: {init_color}")

    if init_color is not None:
        move('turn left',2,60)
    return init_color

def find_color_box(init_color, speed=60):

    while True:
        try:
            move('turn left',1,speed)
          
            n = Vilib.detect_obj_parameter['color_n']
            
            print("n: ", n)
            
            if n == 0:                
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

        except KeyboardInterrupt:
            print("\nCtrl+C pressed...")
        finally:
            Bala7a.do_step('sit', 40)


def main():

    speed = 60

    Bala7a.do_step('stand', 40)

    # Start camera and display
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    

    init_color = get_initial_color()
    find_color_box(init_color, speed)

if __name__ == "__main__":
    main()
