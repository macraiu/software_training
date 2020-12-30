""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 """

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

 #NOT MINE. TAKEN FROM LEETOCODE SOLUTION

 #   stack = []
  #  mapping = {")": "(", "}": "{", "]": "["}
   # for char in s:
    #    print(stack)
     #   if char in mapping:
      #      if mapping[char] != stack.pop():
       #         return False
        #else:
         #   stack.append(char)

  #  return not stack


print(isValid("([[]])"))