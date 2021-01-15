""" 
Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Example 2:

Input: palindrome = "a"
Output: ""
 """

def breakPalindrome(palindrome):
    if len(palindrome) > 1: 
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:] 
        return palindrome[:-1] + 'b'
    return ''

print(breakPalindrome('abccba'))
print(breakPalindrome('aba'))

print(breakPalindrome('bbb'))
print(breakPalindrome('bab'))
print(breakPalindrome('aaa'))
print(breakPalindrome('aa'))
print(breakPalindrome('bb'))
print(breakPalindrome('zaz'))


