import networkx as nx
import matplotlib.pyplot as plt


class Graph_creation:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_lst = {}
        self.G = nx.Graph()
        for node in nodes:
            self.adj_lst[node] = []

    def add_edge(self, u, v):
        self.adj_lst[u].append(v)
        self.adj_lst[v].append(u)
        self.G.add_edge(u, v)

    def print_adj(self):
        print(self.adj_lst)

    def draw(self):
        nx.draw(self.G, node_color='lightgreen',with_labels=True)
        plt.show()


nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
edges = [
    ("A", "B"), ("A", "D"), ("B", "C"), ("D", "E"), ("D", "F"), ("E", "F"), ("E", "G"), ("F", "H"), ("G", "H")
]
graph = Graph_creation(nodes)

for u, v in edges:
    graph.add_edge(u, v)

graph.print_adj()
graph.draw()


