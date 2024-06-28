from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Uncomment this line for undirected graph

    def print_graph(self):
        for node in self.graph:
            print("Adjacency list of node", node)
            print(" -> ".join(map(str, self.graph[node])))
            print()

# Contoh penggunaan:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    g.print_graph()
