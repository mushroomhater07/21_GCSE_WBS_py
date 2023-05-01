from time import sleep
from random import uniform
from sys import exit
import time

def time_convert(sec):
  sec = sec % 60
  print("Time Lapsed = {0}".format(sec))

left_name = input('left player name is ')
right_name = input('right player name is ')

print("press enter after you see GO")
sleep(uniform(2, 5))
start_time=time.time()
input("-----======GO=======-----")
left_time=time.time()
reduced_left = left_time - start_time
print("left time: " , reduced_left)
time_convert(reduced_left)
