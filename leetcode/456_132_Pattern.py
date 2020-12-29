""" Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution? """

def find132pattern(nums):
    print(nums)
    pos_grad = []
    min_ = nums[0]
    max_ = nums[0]
    for i in range(1, len(nums)
        if nums[i] > max_ :
            max_ = nums[i]
        if nums[i] < min_:
            pos_grad.append([min_ + 1, max_ -1])

            min_ = nums[i]
            max_ = nums[i]
        print(pos_grad)
    return False


print(find132pattern([1,2,3,100,2]))