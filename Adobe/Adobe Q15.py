# Given two library versions of an executable: 
# for example, “10.1.1.3” and “10.1.1.9” or “10” and “10.1”. 
# Find out which one is more recent? Strings can be empty also.

def latestVer(first,second):
    lengthF = len(first)
    lengthS = len(second)
    for i in range(min(lengthF,lengthS)):
        if first[i]>second[i]:
            return first
        elif first[i]<second[i]:
            return second
    if lengthF>lengthS:
        return first
    return second
    
print(latestVer('10.1','10.1.2'))