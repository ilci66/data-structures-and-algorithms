# TODO: Perform DFS, push node to stack before returning

# TODO: Find the transpose graph by reversing the edges (create another graph)

# TODO: Pop nodes oen by one from stack and again do DFS on modified (new) graph, each successful DFS gives 1 -> SCC
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, s, e):
        self.graph[s].append(e)

    def stack_order(self, visited, stack, v):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.stack_order(visited, stack, i)
        stack.append(v)

    def transpose(self, visited, v):
        newG = Graph(self.V)

        # for i in self.graph:


    def dfs(self, visited, v):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(visited, v)

    def get_scc(self):
        visited = [False] * self.V
        stack = []

        for v in self.graph:
            if not visited[v]:
                self.stack_order(visited, stack, v)


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
