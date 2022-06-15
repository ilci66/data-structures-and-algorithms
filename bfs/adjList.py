class AdjNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [None] * self.V

    def add_edge(self, v, e):
        node = AdjNode(e)
        node.next = self.adj[v]
        self.adj[v] = node

        node = AdjNode(v)
        node.next = self.adj[e]
        self.adj[e] = node


    def bfs(self, n, visited = None):
        if visited is None:
            visited = []

        if n is not None and n not in visited:
            visited.append(n)

        for i in range(self.V):

            temp = self.adj[visited[i]]

            while temp is not None:
                if temp is not None and temp.val not in visited:
                    visited.append(temp.val)

                temp = temp.next

        return visited

    def print_list(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.adj[i]
            while temp:
                print(" -> {}".format(temp.val), end="")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":
    V = 9

    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(3, 8)
    graph.add_edge(2, 7)
    graph.add_edge(1, 4)
    graph.add_edge(4, 6)
    graph.add_edge(4, 5)


    # graph.print_list()

    print(graph.bfs(0))