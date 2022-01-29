import math
def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    while left<right:
        hours = 0
        mid = (left+right)//2
        for pile in piles:
            hours += math.ceil(pile/mid)
        
        if hours<=h:
            right = mid

        else:
            left = mid+1
    return right

def minEatingSpeed2(piles, h):
    low = 1
    high = max(piles)
    if len(piles)==high:
        return high
    # if len(piles)==1:
    #     return piles[0]//h + (1 if piles[0]%h!=0 else 0)
    def check(piles, val):
        total = 0
        # for i in range(len(piles)):
        #     temp = piles[i]//val + (1 if piles[i]%val!=0 else 0)
        #     total+=temp
        #     print("done",val,"total",total)
        for pile in piles:
                total += math.ceil(pile / val)
        return total
    
    def binarySearch(piles,low,high,h):
        if high==low:
            return high

        if high>low:
            mid = (high+low)//2
            print("mid",mid)
            total = check(piles,mid)
            if total<=h:
                print("first","mid",mid)
                mid = min(mid,binarySearch(piles,low,mid-1,h)) 
                return mid
        
            if total>h:
                print("second")
                return binarySearch(piles,mid+1,high,h)
            
        else:
            return -1

    return binarySearch(piles,low,high,h)+1
                

# print(minEatingSpeed([1,1,1,999999999],10))
# print(minEatingSpeed([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184],\
#     823855818))
print(minEatingSpeed([312884470],312884469))