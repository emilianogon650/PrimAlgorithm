import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a graph
G = nx.Graph()

# Add 20 nodes
num_nodes = 20
G.add_nodes_from(range(num_nodes))

# Randomly connect nodes with weights
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < 0.3:
            weight = random.randint(1, 20)
            G.add_edge(i, j, weight=weight)

# Apply Prim's algorithm via minimum_spanning_tree
mst = nx.minimum_spanning_tree(G, algorithm='prim')

# Print MST edges
print("Minimum Spanning Tree edges:")
total_weight = 0
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v} (weight {data['weight']})")
    total_weight += data['weight']

print(f"\nTotal weight of MST: {total_weight}")

# Optional: visualize
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='lightblue', with_labels=True)
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='red', width=2)
plt.title("Minimum Spanning Tree (Prim's Algorithm)")
plt.show()
