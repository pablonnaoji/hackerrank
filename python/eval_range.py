#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    eval_range = range(2,6)
    eval_range2 = range(6,20)
    if n % 2 == 1:
        print("Weird")
    if n % 2 == 0 and n in eval_range:
        print("Not Weird")
    if n % 2 == 0 and n in eval_range2:
        print("Weird")
    if n % 2 == 0 and n > 20:
        print("Not Weird")