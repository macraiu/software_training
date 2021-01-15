""" 
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 """
def isBoomerang(points):
    (x0,y0), (x1,y1), (x2,y2) = points
    if (y1-y0)*(x2-x1) != (y2-y1)*(x1-x0):
        return True
    return False

print(isBoomerang([[1,1],[2,2],[3,3]]))
print(isBoomerang([[1,1],[2,3],[3,2]]))
