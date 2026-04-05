from time import sleep
from picrawler import Picrawler

Bala7a = Picrawler()

from GameState import MAX_SECTORS, current_sector, lives, map_pieces


# Moving to next sector
def sectorNavigation():
    global current_sector

    current_sector += 1

    if current_sector > MAX_SECTORS:
        print("Congratulations! You've completed all sectors!")
        # craete a end game clebration function here
        return False
    
    if current_sector == 2:
        print("Moving to Sector 2: The Maze")
        move_to_next_sector()

    elif current_sector == 3:
        print("Moving to Sector 3: The Final Challenge")
        move_to_next_sector()

    return True

def move_to_next_sector():
    # stand
    Bala7a.do_action('stand', 40)
    sleep(1)

    # turn right 90 degrees
    Bala7a.do_action('turn right', 1, 60)
    sleep(1)

    # move forward for 4 steps
    Bala7a.do_action('forward', 4, 60)
    sleep(1)

    # turn left 90 degrees
    Bala7a.do_action('turn left', 1, 60)
    sleep(1)

    # sit
    Bala7a.do_action('sit', 40)
    