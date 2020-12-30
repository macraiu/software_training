""" 
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).


 """

def mypow(x, n):

    # from leetcode most upvoted solution
    # indeed is elegant
    # spliting the power to lower and lower 
    # x^20 = x^10 * x^10
    # x^10 = x^5 * x^5
    # x^5 = x^2 * x^2 ^ x
    
  
    if abs(x) < 1e-40:
        return 0 
    if n == 0:
        return 1
    if n < 0:
        return mypow(1/x, -n)
    
    lower = mypow(x, n//2)
    if n % 2 == 0:
        return lower*lower
    if n % 2 == 1:
        return lower*lower*x



a = 2
b = -19
print('final',mypow(a, b))
print('gt', a**b)
