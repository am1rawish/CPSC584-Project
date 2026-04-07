import ColorDetection
import return_to_white_box
from time import sleep

def test_reverse():

    # start robot
    ColorDetection.Bala7a.do_action('stand', 1)

    # start camera
    ColorDetection.Vilib.camera_start(vflip=False, hflip=False)
    ColorDetection.Vilib.display(local=True, web=True)

    sleep(2)

    print("Detecting color...")
    color = ColorDetection.detect_color()

    if color is None:
        print("No color detected")
        return

    print(f"Detected Color: {color}")

    # CLEAR OLD HISTORY (IMPORTANT)
    ColorDetection.move_history.clear()

    # move to color
    aligned = ColorDetection.align_to_color(color)

    if not aligned:
        print("Failed to align")
        return

    print("Reached box!")

    sleep(2)

    # NOW TEST REVERSE
    return_to_white_box.return_to_white_box()


if __name__ == "__main__":
    test_reverse()