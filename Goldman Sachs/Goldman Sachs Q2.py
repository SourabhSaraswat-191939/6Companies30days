# Overlapping rectangles

# Approach 1 -> using Position check
def doOverlap(L1, R1, L2, R2):
        if (L1[0]>L2[0] and L1[0]>R2[0]) or (R1[0]<L2[0] and R1[0]<R2[0]) or (L1[1]<L2[1] and L1[1]<R2[1]) or (R1[1]>L2[1] and R1[1]>R2[1]):
            return 0
        return 1
    
# Approach 2 -> using Check Area

L1=(0,10)
R1=(10,0)
L2=(5,5)
R2=(15,0)
print(doOverlap(L1,R1,L2,R2))