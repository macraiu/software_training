""" 
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
Example 3:

Input: nums = [1], index = [0]
Output: [1]
 """

def createTargetArray2(nums, index):
    d = {}
    for i in range(len(index)):
        if index[i] not in d:
            d[index[i]] = nums[i]
            continue
        
        tmp_prev = d[index[i]]
        d[index[i]] = nums[i]

        for idx in range(index[i] + 1, len(nums)):    
            if idx not in d:
                d[idx] = tmp_prev
                break

            tmp_next = d[idx]
            d[idx] = tmp_prev
            tmp_prev = tmp_next

    l = [0] * len(d)
    for i in range(len(d)):
        l[i] = d[i] 

    return l



def createTargetArray(nums, index):
    l = []
    for i in range(len(index)):
        l.insert(index[i], nums[i])
    return l


print(createTargetArray(nums = [9,8,7,6,5,4], index = [0,1,0,1,0,1])) 
        
