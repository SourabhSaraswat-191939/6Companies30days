# Bridge edge in a graph 

#User function Template for python3

from queue import Queue
def isBridge(V, adj, c, d):
    try:
        adj[c].remove(d)
    except:
        return 0
        
    try:
        adj[d].remove(c)
    except:
        return 0
    # print(adj[c])
    # print(adj[d])
    visited = set()
    queue = Queue()
    queue.put(c)
    while not queue.empty():
        out = queue.get()
        visited.add(out)
        for neighbour in adj[out]:
            if neighbour not in visited:
                queue.put(neighbour)
    # print(len(visited),V)
    if d not in visited:
        return 1
    return 0