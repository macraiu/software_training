""" 
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
 """

def add_one(x):

    for n in reversed(range(len(x))):
        if x[n] + 1 > 9:
            x[n] = 0
        else:
            x[n] += 1
            return x
    
    x.insert(0, 1)
    return x

    
print(add_one([0, 0]))