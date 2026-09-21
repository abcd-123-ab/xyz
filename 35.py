from collections import deque

def bfs(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city == end:
            return path

        if city not in visited:
            visited.add(city)

            for neighbor in graph[city]:
                if neighbor not in visited:
                    queue.append(path + [neighbor])

graph = {
    'Ahmedabad': ['Vadodara', 'Rajkot'],
    'Vadodara': ['Ahmedabad', 'Surat'],
    'Rajkot': ['Ahmedabad', 'Jamnagar'],
    'Surat': ['Vadodara', 'Mumbai'],
    'Jamnagar': ['Rajkot'],
    'Mumbai': ['Surat']
}

print("Shortest Route:")
print(bfs(graph, 'Ahmedabad', 'Mumbai'))