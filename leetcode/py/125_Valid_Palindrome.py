""" 
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 """

def isPalindrome(s):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    a = [x for x in s if x in letters]
    return a == a[::-1] 

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome('0P'))

