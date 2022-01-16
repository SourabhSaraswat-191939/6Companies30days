# Find all the unique quadruple from the given array that sums up to the given number.

# Time Complexity: O(n^3)
def fourSum(arr, k):
    n = len(arr)
    arr.sort()
    result = []
    
    for i in range(n-3):
        for j in range(i+1,n-2):
            l = j+1
            r = n-1
            while (l<r):
                add = arr[i]+arr[j]+arr[l]+arr[r]
                if add==k:
                    result.append([arr[i],arr[j],arr[l],arr[r]])
                    l+=1
                    r-=1
                elif add<k:
                    l+=1
                else:
                    r-=1

    return result


# Time Complexity: O(n^4)
def fourSum2(arr,k):
    n = len(arr)
    arr.sort()
    result = []
    def sum(i,count,val,temp):
        if count==4:
            if val==k:
                result.append(temp.copy())
            return
        if i>=n:
            return
        if arr[i]>(k-val):
            return

        for j in range(i,n):
            temp.append(arr[j])
            sum(j+1,count+1,val+arr[j],temp)
            temp.pop()
    
    for i in range(n-3):
        sum(i+1,1,arr[i],[arr[i]])    

    hashed = list(set(tuple(x) for x in result))
    hashed.sort()
    return hashed

# print(fourSum([0,0,2,1,1],3))
# print(fourSum([10,2,3,4,5,7,8],23))  

n, k=map(int,input().split())
a=list(map(int,input().strip().split()))[:n]
print(fourSum(a,k))
print(fourSum2(a,k))