from picrawler import Picrawler
from time import sleep
from vilib import Vilib
from ColorDetection import move_history, Bala7a, detect_color

def reverse_moves(action):
    if action == 'forward':
        return 'forward'
    elif action == 'backward':
        return 'backward'    
    elif action == 'turn left':
        return 'turn right'
    elif action == 'turn right':
        return 'turn left'
    elif action == 'turn left angle':
        return 'turn right angle'
    elif action == 'turn right angle':
        return 'turn left angle'
    else:
        return None

def align_to_color_back(color):

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

        if x < 250:
            move('turn left angle',1,45)
            print("Color position l:", x)
            continue
      
        elif w < 440:
            move('forward', 2, 60)
            print("Color distance f:", w)
            continue
        
        elif w < 470:
            move('forward', 1, 60)
            print("Color distance f(1):", w)
            continue

        elif x > 480:
            move('turn right angle',1,45)
            print("Color position right:", x)
            continue

        elif w > 550:
            Bala7a.do_action('backward', 1, 60)
            print("Color distance b:", w)

        else:
            print("Final position:", x)
            print("Final distance:", w)
            is_aligned = True
            print("Aligned with color!")
            Bala7a.do_step('sit', 40)
            break

    return is_aligned


def return_to_white_box():
    sleep(2)

    print("Move history:", move_history, "\n")

    print("Returning to white box...\n")

    Bala7a.do_step('stand', 1)

    init_color = detect_color()
    sleep(1)
    while init_color is None:
        print("No color detected, looking")
        init_color = detect_color()

    
    Bala7a.do_action('turn right angle', 2, 60)
    

    # Reverse the move history and execute the opposite actions
    for action, step, speed in move_history:  # Reverse the move history
        opposite_action = reverse_moves(action)

        if opposite_action is None:
            continue   

        print(f"reversing: {action} to {opposite_action}, step {step}, speed {speed}")
        Bala7a.do_action(opposite_action, step, speed)

        Vilib.color_detect(init_color)
        sleep(0.5)  
        
        n = Vilib.detect_obj_parameter.get('color_n', 0)

        if n > 0:
            print(f"Detected color during return: {init_color}")

            if align_to_color_back(init_color):
                print("Aligned with color during return!")
                break    

    # Clear the move history after returning to the white box
    move_history.clear()
    print(" returned to white box")

    Bala7a.do_step('sit', 40)

if __name__ == "__main__":
    return_to_white_box()