class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(self.V)]

    def add_edge(self, x, y):
        self.adj[x].append(y)

    def dfs(self, start):

        visited = []
        print(visited)

        # stack= []
        #
        # if start not in visited:
        #     visited.append(start)
        #
        # for x in self.adj[start]:
        #     while(len(stack)):
        #

    def print_graph(self):
        print(self.adj)

g = Graph(4)
g.add_edge(0, 1);
g.add_edge(0, 2);
g.add_edge(0, 3);
g.add_edge(1, 2);

g.print_graph()
g.dfs(0)