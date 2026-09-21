def dfs(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

visited = set()

if dfs(graph, 'A', visited, None):
    print("Cycle is Present")
else:
    print("Cycle is Not Present")