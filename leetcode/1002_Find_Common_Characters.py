""" 
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 """

def commonChars(A):
    
    d = {}
    for n in range(len(A)):
        for letter in A[n]:
            if letter not in d:
                d[letter] = [0]*len(A)
                d[letter][n] += 1
            else:
                d[letter][n] += 1
                
    out = []
    for i in d:
        out += i * min(d[i])

    return out

print(commonChars(['bella', 'label', 'roller']))
print(commonChars(['cool','lock','cook']))