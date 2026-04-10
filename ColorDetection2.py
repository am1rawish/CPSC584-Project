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

def get_largest_object(color, samples=10):
    best_area = 0
    best_x = None
    best_w = None

    for _ in range(samples):
        Vilib.color_detect(color)
        sleep(0.5)

        count = Vilib.detect_obj_parameter.get('color_n', 0)

        if count > 0:
            h = Vilib.detect_obj_parameter.get('color_h')
            x = Vilib.detect_obj_parameter.get('color_x')
            w = Vilib.detect_obj_parameter.get('color_w')

            area = w * h

            print("area", area)

            if area > best_area:
                best_area = area
                best_x = x
                best_w = w

    return best_x, best_w, best_area

def align_to_color(color):

    is_aligned = False

    while True:
        Vilib.color_detect(color)
        count = Vilib.detect_obj_parameter.get('color_n',0)
        
        if count == 0:
            print("Lost color")
            is_aligned = False
            break

        if count > 1:
            x, w, area = get_largest_object(color)
        else:
            x = Vilib.detect_obj_parameter.get('color_x')
            w = Vilib.detect_obj_parameter.get('color_w')

        if x is None: 
            print("No valid object detected, scanning...")
            is_aligned = False
            break

        print("Color position start:", x) 
        print("Color distance start:", w)

        if x < 200:
            move('turn left angle',1,45)
            print("Color position l:", x)
            continue
      
        elif w < 440:
            move('forward', 2, 80)
            print("Color distance f:", w)
            continue
        
        elif w < 460:
            move('forward', 1, 80)
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
        Bala7a.do_action('turn left angle',3,60)
    return init_color

def find_color_box(init_color, speed=60):

    while True:
        try:
            move('turn left angle',1,speed)
          
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
