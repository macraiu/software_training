""" In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times. """

def repeatedNTimes(A):
    d = set()
    for i in A:
        if i in d:
            return i
        d.add(i)



print(repeatedNTimes([5,1,5,2,5,3,5,4]))
