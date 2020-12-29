""" You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number. """
def nextGreaterElement(nums1, nums2):
    new = [-1] * len(nums1)
    stack = deque()

    for n, i in enumerate(nums1):
        for x in range(n + 1, len(nums2)):
            if i < nums2[x]:
                new[n] = nums2[x]
                break
            
    return  new




nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))