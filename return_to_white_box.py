import ColorDetection
from picrawler import Picrawler
from time import sleep

Bala7a = Picrawler()

def reverse_moves(action):
    if action == 'forward':
        return 'backward'
    elif action == 'backward':
        return 'forward'    
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
    
def return_to_white_box():
    print("Returning to white box...")

    # Reverse the move history and execute the opposite actions
    for action, duration, speed in reversed(ColorDetection.move_history):
        opposite_action = reverse_moves(action)

        if opposite_action:
            print(f"reversing: {action} to {opposite_action}")
            Bala7a.do_action(opposite_action, duration, speed)
            sleep(0.5)  # Add a small delay between actions

    # Clear the move history after returning to the white box
    ColorDetection.move_history.clear()
    print(" returned to white box")

if __name__ == "__main__":
    return_to_white_box()