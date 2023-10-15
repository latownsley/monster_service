# Created by Leela Townsley
# A user interface (UI) that either has a button or can receive a user command to
# relay information / get information from pring.py and imgsrv.py
# 10/4/2023
#
#
import time
from tkinter import *
from PIL import Image

finished = False
count = 0


def call_p():
    ''' Generates a new image'''
    with open('prng-service.txt', 'w') as prng_file:
        prng_file.write('run')

    time.sleep(10)

    with open('prng-service.txt', 'r') as prng_file:
        read_file = prng_file.read()

    with open('image-service.txt', 'w') as img_file:
        img_file.write(read_file)

    time.sleep(10)

    with open('image-service.txt', 'r') as img_file:
        img_path = img_file.read()


    print("Take a look at this CUTIE")

    time.sleep(1)

    # open method used to open different extension image file
    img = Image.open(img_path)

    # This method will show image in any image viewer
    img.show()

    print("Just your type, right?\n Right?")
    time.sleep(1)
    print("I mean, if not, we can try again.")


def quit_everything():
    global finished
    finished = True

    with open('image-service.txt', 'w') as img_file:
        img_file.write('done')

    with open('prng-service.txt', 'w') as prng_file:
        prng_file.write('done')

print("Welcome to the first monster dating service.")
time.sleep(1)
print("So you're looking for your partner, eh? I can help you with that.\n")

while not finished:

    print("Enter 1 if you want to find the partner of your dreams. Enter 2 if you've already given up.")
    value = input("Response:")

    if value == '1':
        call_p()

    else:
        print("Alas, it was not your time. Perhaps you can try again another time.")
        print("Quitting...")
        quit_everything()