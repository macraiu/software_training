""" 
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 """
import math 

def numIdenticalPairs(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    good_couples = 0
    for i in d:
        if d[i] >= 2:
            #fact(n)/fact(r)*fact(n-r)
            #fact(n)/(2*fact(n-2)
            good_couples += math.factorial(d[i])//(2*math.factorial(d[i] - 2))

    return good_couples

print(numIdenticalPairs([1, 2,3,3, 1, 1]))
        