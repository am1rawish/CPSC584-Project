from color_detection import start_camera, detect_color
from time import sleep

start_camera()

while True:

    if detect_color("red"):
        print("Go to RED path")

    elif detect_color("blue"):
        print("Go to BLUE path")

    elif detect_color("yellow"):
        print("Go to YELLOW path")

    elif detect_color("purple"):
        print("Go to PURPLE path")

    sleep(0.2)