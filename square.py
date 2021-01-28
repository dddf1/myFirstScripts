import sys
import random

num = len(sys.argv)

try:
    square = int(sys.argv[1]) if num > 1 else 10
    if square >=2:
        for i in range(square):
            print("* " * square)

    else:
        print("Number of cubes should be at least 2")


except ValueError:
    print("No.. input is not a number. It's a string")