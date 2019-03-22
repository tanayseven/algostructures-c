#!/usr/bin/env python3
import random
import datetime
import sys

def generate_numbers(total, digits=3):
    total = int(total)
    random.seed(datetime.datetime.now())
    return [int(10**digits*random.random()) for n in range(total)]

print(*generate_numbers(sys.argv[1]), sep=' ')

