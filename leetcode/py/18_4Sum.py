""" 
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 """

from collections import Counter
from itertools import *


def fourSum2(nums, target):
    nums.sort()
    quadruplets = set()
    for i in range(len(nums)):
        for j in range(i +1,  len(nums)):
            for k in range(j+1, len(nums)):
                for l in range(k+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quadruplets.add((nums[i],nums[j],nums[k],nums[l]))
    
    return list(quadruplets)

def fourSum(nums, target):
    
    d = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            s = nums[i] + nums[j]
            if s not in d:
                d[s] = [(i,j)]
            else:
                d[s].append((i,j))
    
    a = set()
    for sums in d:
        if target - sums in d:
            for i,j in d[sums]:
                for k,l in d[target - sums]:
                    if len(set([i,j,k,l])) == 4:
                        a.add((sorted([nums[i], nums[j], nums[k], nums[l]]))

    return a

def fourSum3(nums, target):
    nums.sort()
    c = set(combinations(nums, 4))
    print(c)
    return a


#print(fourSum([1,0,-1,0,-2,2], 0))
#print(fourSum([-1,1,1,2,2,-2,-1], 0))

#print(fourSum([-2,-1,-1,1,1,2,2], 0))
print(fourSum([-2,-1,-1,1,0,0,0,0,1,2,2], 1))
print(fourSum([-2,-1,-1,1,0,0,0,0,1,2,2], 0))