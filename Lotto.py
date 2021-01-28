import random
import sys

argNum = len(sys.argv)

try:
    cubesInTofes = int(sys.argv[1]) if argNum > 1 else 10
    if cubesInTofes >= 1 and cubesInTofes <= 14:
        for i in range (cubesInTofes):
            nums = random.sample(range(1 , 50), 6)
            nums.sort()
            misparNosaf = random.sample(range(1 , 8), 1)
            print(f"{nums[0]:2} {nums[1]:2} {nums[2]:2} {nums[3]:2} {nums[4]:2} {nums[5]:2}  {misparNosaf}")
    else:
        print("Number of cubes should be 1 - 14")
except ValueError:
    print("No.. input is not a number. It's a string")