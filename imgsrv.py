# Created by Leela Townsley
# A program that, given a non-negative integer i, returns the
# ith image in a set (order doesn’t matter)
# (Image Service)
# Note: If i is >= the number of images, modulo i by the size of the image set
# 10/4/2023
#
#
import time

finished = False

while not finished:
    time.sleep(5)
    with open('image-service.txt', 'r') as img_file:
        read_file = img_file.read()

    if read_file == 'done':
        finished = True

    if read_file.isnumeric():
        image_num = int(read_file)
        image_num = image_num % 721
        image_num = str(image_num)
        path = '/Users/latownsley/Desktop/361-SoftwareEngineering/1.5Assignment/pokemon/'
        path = path + image_num + '.png'
        with open('image-service.txt', 'w') as img_file:
            img_file.write(path)



