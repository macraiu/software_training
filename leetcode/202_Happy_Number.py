""" Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not. """


def isHappy(n):

    flag = 0
    result = 0
    while result != 1:
        result = 0
        for x in range(len(str(n))):
            result += (n % 10)**2 
            n //= 10 
        if flag == 8:
            return False
        n = result
        flag += 1
    return True

print(isHappy(100))