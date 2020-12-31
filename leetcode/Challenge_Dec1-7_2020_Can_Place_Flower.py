
""" 
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 """


def canP(flowerbed, n):

    if len(flowerbed) == 1 and 0 in flowerbed and n == 1:
        return True

    for idx in range(len(flowerbed)-1):
        if idx == 0 or idx == len(flowerbed) - 2:
            if not (flowerbed[idx] or flowerbed[idx + 1]):
                flowerbed[idx] = 1
                n -= 1
        else:
            if not (flowerbed[idx-1] or flowerbed[idx] or flowerbed[idx+1]):
                flowerbed[idx] = 1
                n -= 1

    if n <= 0:
        return True
    else:
        return False

        
    


print(canP([1, 0, 0,0, 0, 0, 1, 0, 0], 2))
