""" Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

 """
def moveZeroes2(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    
    topop = []
    for n, i in enumerate(nums):
        if i == 0:
            topop.append(n)

    for pop in topop[::-1]:
        nums.pop(pop)

    nums += [0] * len(topop)


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    
    for n in reversed(range(len(nums))):
        if nums[n] == 0:
            nums.pop(n)
            nums.append(0)



a = [0,0,1, 0, 10, 0]
moveZeroes(a)
print(a)