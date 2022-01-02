# Program to find Nth Ugly Number.

def getNthUglyNo(n):
    count = 0
    i=0
    dp = {1:True,2:True,3:True,5:True}
    
    while count<n:
        check = None
        val = i

        while True:
            if val in dp:
                if dp[val]==True:
                    dp[i] = True
                    check = True
                    break
                else:
                    dp[i] = False
                    check = False
                    break

            if val%2==0:
                val=i/2
            else:
                check = False
                break

        if check:
            continue

        while True:
            if val in dp:
                if dp[val]==True:
                    dp[i] = True
                    check = True
                    break
                else:
                    dp[i] = False
                    check = False
                    break

            if val%3==0:
                val=i/2
            else:
                check = False
                break
        if check:
            continue
            
        while True:
            if val in dp:
                if dp[val]==True:
                    dp[i] = True
                    check = True
                    break
                else:
                    dp[i] = False
                    check = False
                    break

            if val%2==0:
                val=i/2
            else:
                check = False
                break
        
        # if i%2==0 or i%3==0 or i%5==0:
        #     count+=1
        i+=1
    return i

print(getNthUglyNo(10))