# Array Pair Sum Divisibility Problem

def canPair(nums, k):
    hashing = {}
    for i in nums:
        val = i%k
        if val not in hashing:
            hashing[val] = 0
        hashing[val] += 1
    
    for i in nums:
        val = i%k
        if hashing[val]==0:
            continue
        hashing[val] -= 1
        mod = (k - val%k)%k
        if mod in hashing:
            if hashing[mod]>0:
                hashing[mod] -= 1
            else:
                return False
        else:
            return False
    
    return True
    
print(canPair([2,4,1,3],4))