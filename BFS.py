import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


class GraphCreation:
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
        nx.draw(self.G, with_labels=True)
        plt.show()

    def BFS(self):
        self.visited = {}
        self.level = {}
        self.parent = {}
        self.bfs_traversal_output = []
        self.queue = Queue()

        for node in self.adj_lst.keys():
            self.visited[node] = False
            self.parent[node] = None
            self.level[node] = -1

        self.source = "A"
        self.visited[self.source] = True
        self.level[self.source] = 0
        self.queue.put(self.source)

        while not self.queue.empty():
            self.u = self.queue.get()
            self.bfs_traversal_output.append(self.u)

            for v in self.adj_lst[self.u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.parent[v] = self.u
                    self.level[v] = self.level[u] + 1
                    self.queue.put(v)
        print(self.bfs_traversal_output)


nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
edges = [
    ("A", "B"), ("A", "D"), ("B", "C"), ("D", "E"), ("D", "F"), ("E", "F"), ("E", "G"), ("F", "H"), ("G", "H")
]
graph = GraphCreation(nodes)

for u, v in edges:
    graph.add_edge(u, v)

graph.print_adj()
graph.draw()
graph.BFS()