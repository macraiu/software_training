
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, S):
    # write your code in Python 3.6
    fam = 0
    if S == "":
        return 2 * N

    col_to_num = {'A': 0, 'B':1, 'C':2,   'D':3, 'E':4, 'F':5, 'G':6,   'H':7, 'J':8, 'K':9}
    row_dict = {}
    for seat in S.split(" "):
        if int(seat[0]) not in row_dict:
            row_dict[int(seat[0])] = [col_to_num[seat[1]]]
        else:
            row_dict[int(seat[0])].append(col_to_num[seat[1]])

    print(row_dict)
    for i in range(1, N+1):
        if i not in row_dict:
            fam += 2
        else:
            #print([x for x in set(row_dict[i]) if x not in set([5,6,7,8])])
            if ([x for x in set(row_dict[i]) if x in set([1,2,3,4])]) == []:
                print("first")
                fam += 1
            if ([x for x in set(row_dict[i]) if x in set([5,6,7,8])]) == []:
                print("second")
                fam += 1
                continue
            if ([x for x in set(row_dict[i]) if x in set([3,4,5,6])]) == []:
                print("third")
                fam +=1
            
    return fam


print(solution(5, '1A 1C 1J'))