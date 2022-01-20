# Find a continuous sub-array which adds to a given number S.



def subArraySum(arr, n, s): 
    start=0
    end = 0
    add = arr[0]
    while True:
        if add==s:
            print("done1")        
            return [start+1,end+1]
        
        elif add>s:
            while add>s and start<n:
                add -= arr[start]
                start+=1
                if start>=n:
                    break

        else:
            end +=1
            if end>=n:
                break
            add += arr[end]
    
    return [-1]


print(subArraySum([1,2,3,7,5],5,12))