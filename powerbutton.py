import os
import time
import RPi.GPIO as GPIO

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:

        GPIO.wait_for_edge(3, GPIO.RISING)
        time.sleep(0.2)
        if GPIO.input(3) == 1:
            os.system('sudo shutdown -h now')

