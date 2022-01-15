# Find the order of characters in the alien language.

from queue import Queue
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        
def findOrder(dict, N, K):
    if N==1:
        return dict[0]
    adjList = {}
    inDegree = {}
    for i in range(K):
        adjList[chr(97+i)] = []
        inDegree[chr(97+i)] = 0
    
    for i in range(1,N):
        for j in range(min(len(dict[i]),len(dict[i-1]))):
            if dict[i-1][j]!=dict[i][j]:
                adjList[dict[i-1][j]].append(dict[i][j])
                inDegree[dict[i][j]] +=1
                break
    
    queue = Queue()
    for key,val in inDegree.items():
        if val==0:
            queue.put(key)

    topo = []
    while not queue.empty():
        out = queue.get()
        topo.append(out)
        for neighbour in adjList[out]:
            inDegree[neighbour] -= 1
            if not inDegree[neighbour]:
                queue.put(neighbour)

    if len(topo)==len(adjList):
        x= ''
        for s in topo:
            x+=s
        return x

    return ''
   
        
N, K = map(int,input().strip().split())
alien_dict = [x for x in input().strip().split()]

print(findOrder(alien_dict,N,K))