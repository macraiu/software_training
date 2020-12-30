""" 
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 """

def sortedSquares2(nums):

    #248ms

    lnums = len(nums)
    if nums[0] < 0 and nums[-1] < 0:
        for n in range(lnums):
            nums[n] = nums[n] * nums[n]
        nums.reverse()
        return nums

    elif nums[0] >= 0 and nums[-1] >= 0:
        for n in range(lnums):
            nums[n] = nums[n] * nums[n]
        return nums

    stidx = 0
    endidx = lnums
    a = []
    while endidx - stidx != 1:
        idx = stidx + (endidx - stidx) // 2
        if nums[idx] >= 0:
            endidx = idx
        else:
            stidx = idx

    for i in range(lnums):
        if stidx >= 0 and endidx == lnums:
            a.append(nums[stidx]*nums[stidx])
            stidx -= 1
        elif stidx < 0 and endidx < lnums:
            a.append(nums[endidx]*nums[endidx])
            endidx += 1
        else:
            el0 = abs(nums[stidx])
            el1 = nums[endidx]
            if el0 <= el1:
                a.append(el0*el0)
                stidx -= 1
            else:
                a.append(el1*el1)
                endidx += 1

    return a

def sortedSquares(nums):
    # 232ms
    for n, i in enumerate(nums):
        nums[n] = i**2
    return sorted(nums)

def sortedSquares(nums):
    # BEST TIME ON LEETCODE
    # 224ms
    for n in range(len(nums)):
        nums[n] = nums[n]**2
    return sorted(nums)

def sortedSquares(nums):
    # 236ms
    for n, i in enumerate(nums):
        nums[n] = i**2
    nums.sort()
    return nums

print(sortedSquares([-40,-10,-8, -4, -2, -1, 0, 3,10]))

