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

