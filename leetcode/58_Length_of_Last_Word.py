""" 
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
 """


def lengthOfLastWord(s):
    res = [len(x) for x in s.split() if x]
    if res:
        return res.pop()
    else:
        return 0

print(lengthOfLastWord("  aaaa   d sffs    gtd  "))
