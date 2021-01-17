""" 
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
Example 4:

Input: n = 2, pick = 2
Output: 2
 """
 
def guess(g):
    num = 10
    if g == num:
        return 0
    elif g < num:
        return 1
    else: 
        return -1


def guessNumber(n):
    snum, enum = 1, n
    while enum - snum != 1:
        num = (enum + snum)//2
        res = guess(num)
        if res == 0:
            return num
        elif res > 0:
            snum = num 
        else:
            enum = num

    return snum if guess(snum) == 0 else enum

print(guessNumber(1000))



