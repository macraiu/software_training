""" Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n). """
def thirdMax(nums):
    a = sorted(set(nums))
    if len(a) < 3:
        return max(a)
    else:
        return a[-3]


import time
import random


A = []
for i in range(0,10000):
    n = random.randint(-10000,10000)
    A.append(n)


t0 = time.clock()
print(thirdMax(A))
t1 = time.clock() - t0
print("first ", t1)

def thirdMax2(nums):
    # ONE SUBMISSIONS WITH GOOD TIME

    # Make a Set with the input.
    nums = set(nums)

    # Find the maximum.
    maximum = max(nums)

    # Check whether or not this is a case where
    # we need to return the *maximum*.
    if len(nums) < 3:
        return maximum

    # Otherwise, continue on to finding the third maximum.
    nums.remove(maximum)
    second_maximum = max(nums)
    nums.remove(second_maximum)
    return max(nums)


t0 = time.clock()
print(thirdMax2(A))
t1 = time.clock() - t0
print("second ", t1)

# FOR HIGH VARIANCE IN THE DISTRIBUTION MINE PERFORMS BETTER