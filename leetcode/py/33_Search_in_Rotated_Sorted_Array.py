""" 
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 """

def search(nums, target):

    l = 0
    r = len(nums) - 1

    while (r - l > 1):

        m = (r + l) // 2

        if nums[m] < nums[r]:
            if nums[m] < target <= nums[r]:
                l = m
            else:
                r = m
        else:
            if nums[l] <= target < nums[m]:
                r = m
            else:
                l = m
    
    if nums[l] == target: return l
    elif nums[r] == target: return r
    else: return -1


print(search(nums = [4, 11, 100, 1000, -10, -4, -1], target = 1000))
