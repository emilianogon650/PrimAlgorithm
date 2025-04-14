import heapq
import random

# Generate a random undirected weighted graph with 20 nodes
def generate_graph(num_nodes=20, edge_probability=0.3, min_weight=1, max_weight=20):
    graph = {i: [] for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_probability:
                weight = random.randint(min_weight, max_weight)
                graph[i].append((j, weight))
                graph[j].append((i, weight))
    return graph

# Prim's algorithm using min-heap (priority queue)
def prims_algorithm(graph):
    start_node = 0
    visited = set()
    min_heap = [(0, start_node, -1)]  # (weight, current_node, from_node)
    mst = []
    total_cost = 0

    while min_heap and len(visited) < len(graph):
        weight, current_node, from_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if from_node != -1:
            mst.append((from_node, current_node, weight))
            total_cost += weight
        for neighbor, edge_weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return mst, total_cost

# MAIN
if __name__ == "__main__":
    graph = generate_graph()
    mst, total = prims_algorithm(graph)

    print("Minimum Spanning Tree edges:")
    for u, v, w in mst:
        print(f"{u} -- {v} (weight {w})")
    print(f"\nTotal weight of MST: {total}")