import sys
import random

num = len(sys.argv)

try:
    tri = int(sys.argv[1]) if num > 1 else 10
    if tri >=2:
        i = 0
        while i < tri:
            i += 1
            print(i * "* ") 

    else:
        print("Number of cubes should be at least 2")


except ValueError:
    print("No.. input is not a number. It's a string")


