# O(V + E) as it does simple DFS for given graph.
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def DFSUtil(self, temp, v, visited):
        temp.append(v)
        visited[v] = True
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFSUtil(temp, i, visited)
        return temp


    def connectedComponents(self):
        visited = [False] * self.V
        cc = []
        for i in range(self.V):
            if visited[i] == False:
                temp = []
                cc.append(self.DFSUtil(temp, i, visited))
        return cc


if __name__ == "__main__":
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    print(g.adj)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)

# This code is contributed by Abhishek Valsan
