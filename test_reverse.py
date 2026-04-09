import ColorDetection2
import return_to_white_box
from time import sleep

def test_reverse():

    # start robot
    ColorDetection2.main()

    # NOW TEST REVERSE
    return_to_white_box.return_to_white_box()


if __name__ == "__main__":
    test_reverse()