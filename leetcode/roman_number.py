def roman(s):
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0
    n = 0
    while n < len(s) - 1: 
        if d[s[n]] < d[s[n+1]]:
            sum += d[s[n+1]] - d[s[n]]
            n += 2
        else:
            sum += d[s[n]] 
            n += 1
    
        print(n)
    #sum += d[s[n]] 

    return sum

print(roman('IV'))