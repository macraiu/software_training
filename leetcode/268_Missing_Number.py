""" Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

  """

def missingNumber(nums):
    lnums = len(nums)
    exp = lnums * (lnums + 1) / 2
    gt = sum(nums)
    return int(exp - gt)

print(missingNumber([3,0,1]))
