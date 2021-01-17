def solution(juice, capacity):
    # write your code in Python 3.6
    differences = []
    for i in range(len(juice)):
        differences.append(capacity[i] - juice[i])
    
    mmax = max(differences)
    init = juice[differences.index(mmax)]
    end = capacity[differences.index(mmax)]
    print(init)
    print(end)
    juice.sort()
    jucies = 1
    cap = init
    for i in juice:
        print('i', i)
        print('cap', cap)
        cap += i
        if cap <= end:
            jucies += 1
        else:
            break
    print(differences)
    

    return 1



print(solution([5, 3, 5], [6, 4, 9]))