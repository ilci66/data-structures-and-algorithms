class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.adj = [[0 for i in range(self.V)] for j in range(self.E)]

    def add_edge(self, v, e):
        self.adj[v][e] = 1
        self.adj[e][v] = 1


    def print_graph(self):
        print(self.adj)


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
                # for node in self.adj[x]:
                #     if node not in visited:
                #         stack.append(node)
                for i in range(len(self.adj[x])):
                    if self.adj[x][i] == 1 and i not in visited:
                        stack.append(i)

        return visited

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