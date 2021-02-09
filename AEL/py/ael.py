######################################################
# Given a list A of integers, return the start index #
# of the longest increasing sequence in the list.    #
######################################################

def solution(A):

    idx_n = {}
    c_idx = 0
    idx_n[c_idx] = 1

    for i in range(1, len(A)):

        if A[i] > A[i - 1]:
            idx_n[c_idx] += 1

        else:
            c_idx = i
            idx_n[c_idx] = 1

    return max(idx_n, key=idx_n.get)


A = [30, 10,20, 10, 5, 1]
print(solution(A))