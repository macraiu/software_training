""" 
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 """

def firstUniwChar(s):
    times = []
    for i in s:
        if times == [] or i not in [x[0] for x in times]:
            times.append([i, 1])
        else:
            times[[x[0] for x in times].index(i)][1] += 1

    for n in range(len(times)):
        if times[n][1] == 1:
            return s.index(times[n][0])
    
    return -1

def firstUniqChar(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    for n, i in enumerate(s):
        if d[i] == 1:
            return n
    
    return -1


print(firstUniqChar("lleettccoodee"))