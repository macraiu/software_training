""" Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string. """

def restoreString(s, indices):
    restored = [0] * len(s)
    for n, i in enumerate(indices):
        restored[i] = s[n]
    return "".join(restored)



s = "aiohn" 
indices = [3,1,4,2,0]
print(restoreString(s, indices))