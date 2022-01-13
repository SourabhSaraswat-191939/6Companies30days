def calculateSpan(a,n):
    span = []
    stack = []
    for i in range(n):
        while len(stack)>0 and stack[-1][0]<=a[i]:
            stack.pop()
        if len(stack)==0: 
            span.append(i+1)
        else:
            span.append(i-stack[-1][1])
        stack.append((a[i],i))
    
    return span    

print(calculateSpan([10, 4, 5, 90, 120, 80],6))