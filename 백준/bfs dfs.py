graph = {
    1: [2,5,9],
    2: [3],
    3: [4],
    4: [],
    5: [6,8],
    6: [7],
    7: [],
    8: [],
    9: [10],
    10: []
}
def iterative_dfs(start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        print(' ')
        print("pop=", v)
        if v not in visited:
            visited.append(v)
            print("visted=",visited)
            for w in graph[v]:
                stack.append(w)
                print(stack)
                
    return visited

iterative_dfs(1)

graph = {
    1: [2,3,4],
    2: [5],
    3: [6,7],
    4: [8],
    5: [9],
    6: [10],
    7: [],
    8: [],
    9: [],
    10: []
}

def bfs(start_v):
    visited = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        print('\n',v)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
                print("visited=",visited)
                print("queue=",queue)
    return visited

print("bfs: ", bfs(1))
