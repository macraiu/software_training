import numpy as np
import time
import random


A = []
for i in range(0,100000):
    n = random.randint(-10000,100000)
    A.append(n)

""" t0 = time.clock()

#A = [100,100,1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,4,5,6]
a = min([a for a in range(1, len(A)+2) if a>0 and a not in A])

t1 = time.clock() - t0

print(a)
print("first implementation ", t1)

t0 = time.clock()

A.sort()
min_nr = 1
for a in A:
    if a == min_nr:
        min_nr += 1
    if a > min_nr:
        break

t1 = time.clock() - t0

print(min_nr)
print("second implementation ", t1) """


t0 = time.clock()

set_A = set(A)
A = list(set_A)
A.sort()
min_nr = 1
for a in A:
    if a == min_nr:
        min_nr += 1
    if a > min_nr:
        break

t1 = time.clock() - t0

print(min_nr)
print("third implementation ", t1)