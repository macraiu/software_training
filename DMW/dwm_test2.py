import numpy as np
import time
import random


""" A = []
for i in range(0,10000):
    n = random.randint(-1000,1000)
    A.append(n)


t0 = time.clock()


t1 = time.clock() - t0
print("first implementation ", t1)
"""

S = "aabbccder"
C= [1,5,6,7,10,2,5,6,9]
cost = 0

for index in range(len(S)-1):
    if S[index] == S[index + 1]:
        cost += C[index]

print(cost)
