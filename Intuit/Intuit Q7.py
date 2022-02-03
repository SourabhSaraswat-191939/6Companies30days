# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

def shipWithinDays(weights, days):
    n= len(weights)
    def checkShipCapacity(capacity):
        wt = 0
        daysCount = 1  # because we are starting from 1st day, not 0th day.
        for i in range(n):
            wt+=weights[i]
            if wt>capacity:
                wt = weights[i]
                daysCount+=1
        if daysCount<=days:
            return True
        else:
            return False
        
    ans = 0
    low = max(weights)
    high = sum(weights)
    while low<=high:
        mid = (low+high)//2
        if checkShipCapacity(mid):
            ans = mid
            high = mid-1
        else:
            low = mid+1
            
    return ans

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))