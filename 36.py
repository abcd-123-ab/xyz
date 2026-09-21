def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and i not in visited:
            dfs(graph, i, visited)


graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

print("DFS Traversal:")
dfs(graph, 0)