class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(self.V)]

    def add_edge(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def dfs(self, start):

        visited = []
        print(visited)

        stack= []
        stack.append(start)

        while len(stack):
            x = stack[-1]
            stack.pop()

            if x not in visited:
                visited.append(x)

                for node in self.adj[x]:
                    if node not in visited:
                        stack.append(node)

        return visited

    def print_graph(self):
        print(self.adj)

g = Graph(4)
g.add_edge(0, 1);
g.add_edge(0, 2);
g.add_edge(0, 3);
g.add_edge(1, 2);

g.print_graph()
print(g.dfs(2))