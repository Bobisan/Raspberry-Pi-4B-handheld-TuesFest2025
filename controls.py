#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
import spidev
import uinput

# Pins associated with corresponding button
DPadUp = 24
DPadDown = 7
DPadLeft = 25
DPadRight = 8
Select = 22
Start = 12
AButton = 20
BButton = 21
XButton = 16
YButton = 2
LeftBumper = 23
LeftTrigger = 18
RightBumper = 27
RightTrigger = 4

#set up GPIO Pins for buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(DPadUp, GPIO.IN, pull_up_down=GPIO.PUD_UP) #D-pad up
GPIO.setup(DPadDown, GPIO.IN, pull_up_down=GPIO.PUD_UP) #D-pad down
GPIO.setup(DPadLeft, GPIO.IN, pull_up_down=GPIO.PUD_UP) #D-pad left
GPIO.setup(DPadRight, GPIO.IN, pull_up_down=GPIO.PUD_UP) #D-pad right
GPIO.setup(Select, GPIO.IN, pull_up_down=GPIO.PUD_UP) #select
GPIO.setup(Start, GPIO.IN, pull_up_down=GPIO.PUD_UP) #start
GPIO.setup(AButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) #a
GPIO.setup(BButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) #b
GPIO.setup(XButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) #x
GPIO.setup(YButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) #y
GPIO.setup(LeftBumper, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left bumper
GPIO.setup(LeftTrigger, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left trigger
GPIO.setup(RightBumper, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Right bumper
GPIO.setup(RightTrigger, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Right trigger

#Time delay, which tells how many seconds the value is read out
delay = 0.5


# Creating the virtual gamepad
events = (
	uinput.BTN_DPAD_UP,
	uinput.BTN_DPAD_DOWN,
	uinput.BTN_DPAD_LEFT,
	uinput.BTN_DPAD_RIGHT,
	uinput.BTN_SELECT,
	uinput.BTN_START,
    	uinput.BTN_A,
	uinput.BTN_B,
	uinput.BTN_X,
	uinput.BTN_Y,
	uinput.BTN_TL,
	uinput.BTN_TL2,
	uinput.BTN_TR,
	uinput.BTN_TR2,
)

device = uinput.Device(events)

try:
	while True:

		if GPIO.input(DPadUp) == GPIO.HIGH:
			#print("D-pad up pressed")
			device.emit(uinput.BTN_DPAD_UP, 1)
		else:
			device.emit(uinput.BTN_DPAD_UP, 0)

		if GPIO.input(DPadDown) == GPIO.HIGH:
			#print("D-pad down pressed")
			device.emit(uinput.BTN_DPAD_DOWN, 1)
		else:
			device.emit(uinput.BTN_DPAD_DOWN, 0)

		if GPIO.input(DPadLeft) == GPIO.HIGH:
			#print("D-pad left pressed")
			device.emit(uinput.BTN_DPAD_LEFT, 1)
		else:
			device.emit(uinput.BTN_DPAD_LEFT, 0)

		if GPIO.input(DPadRight) == GPIO.HIGH:
			# print("D-pad right pressed")
			device.emit(uinput.BTN_DPAD_RIGHT, 1)
		else:
			device.emit(uinput.BTN_DPAD_RIGHT, 0)

		if GPIO.input(Select) == GPIO.HIGH:
			#print("Select button pressed")
			device.emit(uinput.BTN_SELECT, 1)
		else:
			device.emit(uinput.BTN_SELECT, 0)

		if GPIO.input(Start) == GPIO.HIGH:
			#print("Start button pressed")
			device.emit(uinput.BTN_START, 1)
		else:
			device.emit(uinput.BTN_START, 0)

		if GPIO.input(AButton) == GPIO.HIGH:
			#print("A button pressed")
			device.emit(uinput.BTN_A, 1)
		else:
			device.emit(uinput.BTN_A, 0)

		if GPIO.input(BButton) == GPIO.HIGH:
			#print("B button pressed")
			device.emit(uinput.BTN_B, 1)
		else:
			device.emit(uinput.BTN_B, 0)

		if GPIO.input(XButton) == GPIO.HIGH:
			#print("X button pressed")
			device.emit(uinput.BTN_X, 1)
		else:
			device.emit(uinput.BTN_X, 0)

		if GPIO.input(YButton) == GPIO.HIGH:
			#print("Y button pressed")
			device.emit(uinput.BTN_Y, 1)
		else:
			device.emit(uinput.BTN_Y, 0)

		if GPIO.input(LeftBumper) == GPIO.HIGH:
			#print("Left bumper up pressed")
			device.emit(uinput.BTN_TL, 1)
		else:
			device.emit(uinput.BTN_TL, 0)

		if GPIO.input(LeftTrigger) == GPIO.HIGH:
			#print("Left trigger up pressed")
			device.emit(uinput.BTN_TL2, 1)
		else:
			device.emit(uinput.BTN_TL2, 0)

		if GPIO.input(RightBumper) == GPIO.HIGH:
			#print("Right bumper up pressed")
			device.emit(uinput.BTN_TR, 1)
		else:
			device.emit(uinput.BTN_TR, 0)

		if GPIO.input(RightTrigger) == GPIO.HIGH:
			#print("Right trigger pressed")
			device.emit(uinput.BTN_TR2, 1)
		else:
			device.emit(uinput.BTN_TR2, 0)

		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	device.destroy()
