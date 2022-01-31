# https://leetcode.com/problems/course-schedule-ii/

from queue import Queue
def findOrder(numCourses, prerequisites):
    inDegree = [0]*numCourses
    adjList = {}
    for course, dependent in prerequisites:
        if dependent not in adjList:
            adjList[dependent] = []
        adjList[dependent].append(course)
        inDegree[course]+=1
        
    queue = Queue()
    for i in range(numCourses):
        if inDegree[i]==0:
            queue.put(i)
    
    topoSort = []
    visited = set()
    while not queue.empty():
        out = queue.get()
        topoSort.append(out)
        visited.add(out)
        if out not in adjList:
            continue
        for neighbour in adjList[out]:
            inDegree[neighbour]-=1
            if (inDegree[neighbour]==0) and (neighbour not in visited):
                queue.put(neighbour)
    print(topoSort)
    return topoSort if len(topoSort)==numCourses else []

findOrder(2,[[1,0]])