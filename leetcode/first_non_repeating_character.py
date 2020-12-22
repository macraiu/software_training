def firstUniwChar(s):
    times = []
    for i in s:
        if times == [] or i not in [x[0] for x in times]:
            times.append([i, 1])
        else:
            times[[x[0] for x in times].index(i)][1] += 1

    for n in range(len(times)):
        if times[n][1] == 1:
            return s.index(times[n][0])
    
    return -1



a = [['l', 2], ['e', 1], ['e', 1], ['t', 1], ['t', 1], ['c', 1], ['o', 1], ['d', 1], ['e', 1]]
print([x[0] for x in a])

print(firstUniwChar("lleetcode"))