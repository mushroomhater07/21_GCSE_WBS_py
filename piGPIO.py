from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit
import time


led = LED(4)
right_button = Button(15)
left_button = Button(14)

led.on()
sleep(uniform(2, 5))
led.off()
start_time = time.time()

def left():
        print("left button pressed")
        L_time = time.time()
        reduced_left = L_time - start_time
        print("left time", reduced_left)
def right():
        print("right button pressed")
        right_time = time.time()
        reduced_right = right_time - start_time
        print("right time: ", reduced_right)
def pressed(button):
    if (reduced_right > reduced_left) :
        print("right won")
    else:
        print("left won")
    exit
right_button.when_pressed = right
right_button.when_pressed = pressed
left_button.when_pressed = left
left_button.when_pressed = pressed
