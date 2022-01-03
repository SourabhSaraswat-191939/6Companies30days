# Find max 10 numbers in a list having 10M entries.

# with a priority queue implemented with a heap, the complexity of insertion to queue is O(log N)
# In the worst case you get 10M*log2(100) which is better than 10M*log2(10M)
# In general, if you need the largest K numbers from a set of N numbers, the complexity is O(N log K) rather than O(N log N), this can be very significant when K is very small comparing to N.


import heapq

def maxNumbers(nums, n):
    heap = []

    for i in nums:
        heapq.heappush(heap,i)
        
    print(heap)
    return heapq.nlargest(n,nums)

print(maxNumbers([3,5,4,7,92,24,1,32,65,742,23,44,7,89,3,2,2,654,7,66],5))
