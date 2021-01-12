""" 

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:

Input: s = "ab123"
Output: "1a2b3"
 """

def reformat(s):

    nums = []
    letters = []
    n = '0123456789'
    for i in s: nums.append(i) if i in n else letters.append(i)

    x, y = (letters, nums) if len(letters) <= len(nums) else (nums, letters)
    if len(y) - len(x) > 1: return ''

    final = []
    for i in range(len(x) + len(y)):
        final.append(y[i//2]) if i % 2 == 0 else final.append(x[i//2])

    return ''.join(final)

print(reformat('a0b1c2'))
print(reformat('covid2019'))
print(reformat('ab123'))
print(reformat('a'))
print(reformat('145aa'))
print(reformat('ab1'))
print(reformat('123'))
print(reformat('err'))


