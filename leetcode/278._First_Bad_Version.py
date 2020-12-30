""" 

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 # The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
  """

def isBadVersion(a):
    if a >= 1:
        return True
    else:
        return False

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
   
    stidx = 0
    endidx = n 

    while endidx - stidx != 1:
        if isBadVersion(stidx + (endidx - stidx) // 2) == True:
            endidx = stidx + (endidx - stidx) // 2
        else:
            stidx = stidx + (endidx - stidx) // 2
        
    return endidx


print(firstBadVersion(1))
        
        


