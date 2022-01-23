# Elections

def winner(arr,n):
    votes = {}
    for vote in arr:
        if vote not in votes:
            votes[vote] = 0
        votes[vote]+=1
    result = []
    maxCount = 0
    for name, count in votes.items():
        if count>maxCount:
            result = []
            result.append(name)
            maxCount = count
        if count==maxCount:
            result.append(name)
    
    result.sort()
    return [result[0],votes[result[0]]]

print(winner(['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john'],13))