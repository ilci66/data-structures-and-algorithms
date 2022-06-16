class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.matrix = [[0 for i in range(self.V)] for x in range(self.E)]

    def add_edge(self, s, e):
        self.matrix[e][s] = 1
        self.matrix[s][e] = 1

    def bfs(self, start, visited = None):
        if visited is None:
            visited = []

        if start not in visited:
            visited.append(start)

        queue = []

        for i in range(self.V):
            if self.matrix[start][i] == 1 and i not in visited:
                queue.append(i)

        for x in queue:
            self.bfs(x, visited)

        return visited

    def print_graph(self):
        print(self.matrix)


if __name__ == "__main__":
    V = 4
    E = 4

    graph = Graph(V,E)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph()
    print(graph.bfs(3))