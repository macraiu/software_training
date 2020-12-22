
def add_one(x):

    s = str(int("".join([str(i) for i in x])) + 1)
    
    return [int(x) for x in s]

print(add_one([0,9,8]))