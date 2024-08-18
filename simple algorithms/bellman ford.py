def bellman_ford(graph, vertices, start):
    distances = {v: float('infinity') for v in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distances[u] != float('infinity') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in graph:
        if distances[u] != float('infinity') and distances[u] + w < distances[v]:
            print("Graph contains a negative-weight cycle")
            return None

    return distances

graph = []
vertices = set()
edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    u, v, w = input("Enter the edge (u v w): ").split()
    w = int(w)
    graph.append((u, v, w))
    vertices.add(u)
    vertices.add(v)

start = input("Enter the start node: ")
result = bellman_ford(graph, vertices, start)
if result:
    print(f"Shortest distances from {start}: {result}")
