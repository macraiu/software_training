""" 

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 """

def longcomm(strs):

    prefix = []
    if strs != []:
        for letter_number in range(len(strs[0])):
            for string_index in range(len(strs) - 1):
                try:
                    if strs[string_index][letter_number] != strs[string_index + 1][letter_number]:
                        return ''.join(prefix)
                except:
                    return ''.join(prefix)

            prefix.append(strs[0][letter_number])
    
    if prefix == []:
        return ''
    else:
        return ''.join(prefix)

print(longcomm(["alf", "al", "alfamo"]))