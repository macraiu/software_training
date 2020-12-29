""" Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k. """

def containsNearbyDuplicate2(nums, k):
    
    d = {}
    for n, i in enumerate(nums):
        if i not in d:
            d[i] = []
        d[i].append(n)

        if len(d[i]) >= 2:
            for r in range(len(d[i]) -1):
                if d[i][r+1] - d[i][r] <= k: 
                    return True
            d[i] = [d[i][-1]]    

    return False

def containsNearbyDuplicate(nums, k):
    
    lnums = len(nums)
    if k >= lnums:
        if len(set(nums)) != lnums:
            return True
    else:
        a = set(nums[:k])
        for n in range(lnums - k):
            a.add(nums[n+k])
            if len(a) != k + 1:
                return True
            a.remove(nums[n])
        
    return False

print(containsNearbyDuplicate([1,2,1,4,5,1], 3))