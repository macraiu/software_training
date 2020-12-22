def mypow(x, n):
    num = x
    if n > 0:
        for i in range(1, n):
            num *= x
        return num
    elif n < 0:
        for i in range(1, abs(n)):
            num *= x
        return 1/num
    else:
        return 1


print('final',mypow(0.00001, 1))

print(2**(1/2))