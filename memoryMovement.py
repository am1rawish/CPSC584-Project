from ColorDetection import Bala7a

move_history = []

def memoryMovement(action, duration=1, speed=40):
    Bala7a.do_action(action, duration, speed)

    # Store the action in the move history
    move_history.append((action, duration, speed))
