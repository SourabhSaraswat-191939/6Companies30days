# Count the subarrays having product less than k


# k => target value
def countSubArrayProductLessThanK(a, n, k):
    i=0
    result = 1
    length = n+1
    count = 0
    j=0
    while j<n:
        result *=a[j]
        while i<j and result>=k:
            result //=a[i]
            i+=1    
            
        if result<k:
            count += j-i+1
        j+=1
                    
    return count

print(countSubArrayProductLessThanK([1, 2, 3, 4],4,10))