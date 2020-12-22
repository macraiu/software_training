def sqrt(x):
    if x == 0:
        return 0
    else:
        for i in range(x + 2):
            if i*i > x:
                return i - 1


print(sqrt(0)) 