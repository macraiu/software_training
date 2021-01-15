""" 
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 """



def wordPattern(pattern, s):
    words = s.split(' ')
    couples = [(a, b) for a, b in zip(pattern, words)]
    if len(words) != len(pattern):
        return False
    return len(set(couples)) == len(set(pattern)) == len(set(words)) 


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("a", "dog"))

a = [(1,2), (3,4)]
print(a)
print(2 in a)

        
