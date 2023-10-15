# Created by Leela Townsley
# A program that generates pseudo-random numbers
# 10/4/2023
#
#

import time
import random
from datetime import datetime

random.seed(datetime.now().timestamp())
# Note: time.time() may have only second-level precision on some operating systems.
# datetime.now() creates a seed with microsecond level detail.

finished = False

while not finished:
    time.sleep(5)
    with open('prng-service.txt', 'r') as prng_file:
        read_file = prng_file.read()

    if read_file == 'run':
        random_num = random.randint(0, 10000)
        str_num = str(random_num)
        with open('prng-service.txt', 'w') as prng_file:
            prng_file.write(str_num)

    if read_file == 'done':
        finished = True



