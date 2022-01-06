# Program to find Nth Ugly Number.

# Using DP
def getNthUglyNo(n):
    ugly = [1]
    i2 = i3 = i5 = 0

    for i in range(1,n):
        mini = min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)

        ugly.append(mini)
        if mini == ugly[i2]*2:
            i2+=1
        if mini == ugly[i3]*3:
            i3+=1
        if mini == ugly[i5]*5:
            i5+=1
    
    return ugly[n-1]
print(getNthUglyNo(10))

