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

def iteer(num,visited=[]):
    visited.append(num)
    print(visited,'\n')
    for w in graph[num]:
        if not w in visited:
            visited=iteer(w,visited)
            print(visited)
    return visited

iteer(1)
