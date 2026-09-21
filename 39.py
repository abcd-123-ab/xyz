def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

visited = dfs(graph, 'A')

if len(visited) == len(graph):
    print("Graph is Connected")
else:
    print("Graph is Not Connected")
    