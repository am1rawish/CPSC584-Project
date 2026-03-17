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

def align_to_color(color, moves_log):

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
            moves_log.append('turn left angle')

        if x > 400:
            Bala7a.do_action('turn right angle',1,80)
            print("Color position right:", x)
            moves_log.append('turn right angle')

        if w < 65:
            Bala7a.do_action('turn left', 1, 80)
            Bala7a.do_action('forward', 1, 80)
            print("Color distance f:", w)
            moves_log.append('forward')
        
        if w > 85:
            Bala7a.do_action('backward', 1, 80)
            print("Color distance b:", w)
            moves_log.append('backward')

        elif 200 <= x <= 400 and 65 <= w <= 85:
            print("Final distance:", w)
            print("Final position:", x)
            is_aligned = True
            print("Aligned with color!")
            return False

        else:
            return

    return is_aligned

def reverse_move(moves_log):
    if not moves_log:
        return
    last_move_index = len(moves_log) - 1
    last_move = moves_log[last_move_index]
    

    if last_move == 'turn left angle':
        Bala7a.do_action('turn right angle',1,80)

    elif last_move == 'turn right angle':
        Bala7a.do_action('turn left angle',1,80)
    
    elif last_move == 'forward':
        Bala7a.do_action('backward', 6, 80)

    elif last_move == 'backward':
        Bala7a.do_action('forward', 6, 80)

    elif last_move == 'turn left':
        Bala7a.do_action('turn right',1,80) 

    elif last_move == 'turn right':
        Bala7a.do_action('turn left',1,80)

def main():

    speed = 80

    Bala7a.do_step('stand', 40)

    # Start camera and display
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)

    sleep(1)

    while True:

        color = detect_color()
        moves_log = []
        has_detected = False

        if color is None:
            if has_detected:
                print("Color lost, reversing last move")
                reverse_move(moves_log)
            else:
                print("No color detected, scanning...")
                Bala7a.do_action('turn left',1,speed)
                moves_log.append('turn left angle')

        else: 
            has_detected = True
            print(f"Detected color: {color}")
            
            aligned = align_to_color(color)

            if not aligned:
              print("Failed to align with color, scanning again...")

            else:
                print("Successfully aligned with color!")
                break

if __name__ == "__main__":
    main()
