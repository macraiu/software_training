# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if A != []:
        K = K % len(A)
        return  A[len(A)-K:] + A[:len(A)-K]
    else:
        return []


print(solution([3, 8, 9, 7, 6], 12))