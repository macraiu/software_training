def decrypt(l, k):

    new_l = [0] * len(l)
    if k > 0:
        for n, i in enumerate(l):
            for index in range(0, k):
                new_index = (n + index + 1) % (len(l))
                new_l[n] += l[new_index] 
                print('ln', new_l[n])

    if k < 0:
        for n, i in enumerate(l):
            for index in range(0, abs(k)):
                new_index = (n - index - 1) % (len(l))
                new_l[n] += l[new_index] 
        
        
    return new_l


print(decrypt([5,7,1,4], -2))

