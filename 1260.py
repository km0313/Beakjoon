from collections import deque
import sys
read=sys.stdin.readline
n,m,v=map(int,read().split())
graph={}
for i in range(n):
    graph[i+1]=[]
for i in range(m):
    n1,n2=map(int,read().split())
    if n1 not in graph:
        graph[n1]=[]
    if n2 not in graph:
        graph[n2]=[]
    graph[n2].append(n1)
    graph[n1].append(n2)

for i in graph:
    graph[i]=sorted(graph[i])


def dfs(num,g,visited=[]):
    visited.append(num)
    for w in g[num]:
        if w not in visited:
            visited=dfs(w,g,visited)
            
    return visited

def bfs(num,g,visited=[]):
    q=[]
    q.append(num)
    visited.append(num)
    while q:
        n=q.pop(0)
        for w in g[n]:
            if w not in visited:
                visited.append(w)
                q.append(w)
    return visited
    

print(*dfs(v,graph))
print(*bfs(v,graph))


