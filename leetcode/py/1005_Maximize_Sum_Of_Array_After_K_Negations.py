""" 
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 """


def largestSumAfterKNegations(A, K):
    b = sorted(A)
    print(b)
    i = 0
    while K > 0 and i < len(A) -1:
        if abs(b[i]) <= b[i+1]:
            b[i] = -b[i]
        else:
            b[i] = -b[i]
            i += 1
        K -= 1
    
    if K % 2 != 0:
        b[i] = -b[i]
    
    return sum(b)

print(largestSumAfterKNegations([4, 3, 2], 1))
print(largestSumAfterKNegations([3,-1,0,2], 3))
print(largestSumAfterKNegations([2,-3,-1,5,-4], 2))
print(largestSumAfterKNegations([2], 1))
print(largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6))
print(largestSumAfterKNegations([-8,-5,-3,-5, 1], 6))

print(largestSumAfterKNegations([1,2,22,-23,-9,-30,-6,-9,1,8,24,2,21,29,10,-25,18,30,1,9,-8,-11,-22,-23,-17,-12,19,28,19,28], 24))

