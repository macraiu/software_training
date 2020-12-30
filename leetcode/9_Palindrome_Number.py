""" 
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 """

def isPalindrome2(x):

    # WTIH STRING CONVERSION

    s = str(x)
    if s == s[::-1]:
        return True
    return False

def isPalindrome(x):
    
    # WITHOUT STRING CONVERSION

    if x < 0:
        return False
    
    a = 0
    tmp = x
    while tmp > 0:
        a = a*10 + tmp%10 
        tmp //= 10

    return a == x or x == 0


print(isPalindrome(122))