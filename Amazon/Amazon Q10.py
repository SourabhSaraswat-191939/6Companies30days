# Nuts and Bolts Problem

def matchPairs(nuts, bolts, n):
    hash1 = {}
    bolts.sort()
    for i in range(n):
        hash1[nuts[i]] = i
    
    for i in range(n):
        if (bolts[i] in hash1):
            nuts[i] = bolts[i]
    

N = 5
nuts = ['@', '%', '$', '#', '^']
bolts = ['%','@', '#','$','^']
matchPairs(nuts,bolts,N)
print(nuts)
print(bolts)