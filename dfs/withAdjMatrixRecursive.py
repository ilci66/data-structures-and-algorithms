class Graph:

    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.adj = [[0 for i in range(v)] for j in range(v)]


    def add_edge(self,v,e):
        self.adj[v][e] = 1
        self.adj[e][v] = 1


    def dfs(self, start, visited = None):
        if visited is None:
            visited = []

        visited.append(start)

        for i in range(self.v):

            if self.adj[start][i] == 1 and i not in visited:
                self.dfs(i, visited)

        return visited

    def print_graph(self):
        print(self.adj)

if __name__ == "__main__":
    V = 5
    E = 5

    graph = Graph(V,E)
    graph.print_graph()

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)

    # print("graph ==> ", graph.graph)
    graph.print_graph()
    print(graph.dfs(4))