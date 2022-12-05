import heapq


def dijkstra(graph, start):
    shortest_path = {}  # เก็บค่าที่สั้นที่สุดไปยังโหนดนั้น อัพเดทเรื่อยๆ
    parent = {}  # เก็บโหนด parent
    infinity = 999
    visited = set()
    H = []
    for node in graph:
        shortest_path[node] = infinity

    shortest_path[start] = 0
    heapq.heappush(H, (0, s))

    while H:
        _, u = heapq.heappop(H)
        visited.add(u)
        for v in graph[u]:
            if v in visited:
                continue

            if (shortest_path[u] + graph[u][v] < shortest_path[v]):
                shortest_path[v] = shortest_path[u]+graph[u][v]
                heapq.heappush(H, (shortest_path[u] + graph[u][v], v))
                parent[v] = u

    return shortest_path


def bellman(graph, start):
    shortest_path = {}  # เก็บค่าที่สั้นที่สุดไปยังโหนดนั้น อัพเดทเรื่อยๆ
    parent = {}  # เก็บโหนด parent
    infinity = 999

    for node in graph:
        shortest_path[node] = infinity
    shortest_path[start] = 0
    line = len(shortest_path)
    for i in range(1, line):
        for u in shortest_path:
            for v in graph[u]:
                if (shortest_path[u]+graph[u][v] < shortest_path[v]):
                    shortest_path[v] = shortest_path[u]+graph[u][v]
                    parent[v] = u

    for u in shortest_path:
        for v in graph[u]:
            if (shortest_path[u]+graph[u][v] < shortest_path[v]):
                text = 'can not find shortest paths because of negative-weight cycle'
                return text

    return shortest_path


pos_graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 3, 'D': 8},
    'C': {'D': 2},
    'D': {'E': 11, 'F': 22},
    'E': {'C': 5},
    'F': {'E': 1}
}

neg_graph = {
    'A': {'B': 6, 'C': 4, 'D': 5},
    'B': {'E': -1},
    'C': {'B': -2, 'E': 3},
    'D': {'C': -2, 'F': -1},
    'E': {'F': 3},
    'F': {}
}

neg_cy_g = {
    'A': {'B': 4, 'C': 4, 'D': 3},
    'B': {},
    'C': {'E': -2, 'G': 4},
    'D': {'C': 2, 'A': 3},
    'E': {'B': 3, 'G': -3},
    'F': {'E': 2, 'H': 2},
    'G': {'D': 1, 'F': -2},
    'H': {'G': -2}
}

d_new = {
    'A': {'B': 6, 'C': 4, 'D': 5},
    'B': {'E': 1},
    'C': {'B': 2, 'E': 3},
    'D': {'C': 2, 'F': 1},
    'E': {'F': 3},
    'F': {}
}

s = 'A'

print("Dijkstra Algorithm :     ", dijkstra(neg_graph, s))
print("Bellman-Ford Algorithm : ", bellman(neg_graph, s))
