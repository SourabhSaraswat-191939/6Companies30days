from collections import deque
def isPossible(N,prerequisites):
    adjList = {}
    inDegree = [0]*N
    for i in range(len(prerequisites)):
        if prerequisites[i][0] not in adjList:
            adjList[prerequisites[i][0]] = []
        adjList[prerequisites[i][0]].append(prerequisites[i][1])
        inDegree[prerequisites[i][1]] += 1

    topo = []
    queue = deque()
    for i in range(N):
        if inDegree[i]==0: queue.append(i)
    while queue:
        out = queue.popleft()
        topo.append(out)
        if out not in adjList:
            continue
        for neighbour in adjList[out]:
            inDegree[neighbour] -= 1
            if not inDegree[neighbour]: queue.append(neighbour)
    if len(topo)==N:
        return True
    return False


def isPossible2(self,N,prerequisites):
    adjList = {i:[] for i in range(N)}
    for i in range(len(prerequisites)):
        adjList[prerequisites[i][0]].append(prerequisites[i][1])
    
    visited = set()
    def dfs(task):
        if task in visited:
            return False
        if adjList[task]==[]:
            return True

        visited.add(task)
        for neighbour in adjList[task]:
            if not dfs(neighbour):
                return False
        
        visited.remove(task)
        adjList[task] = []
        return True

    for task in prerequisites:
        if not dfs(task[0]):
            return False
    
    return True


# print(isPossible2(4,[[1,0],[2,1],[3,2]]))
print(isPossible(25,[[0,23],[7,21],[8,0],[8,5],[8,9],[8,12],[9,23],[13,3],[19,24],[23,15]]))




