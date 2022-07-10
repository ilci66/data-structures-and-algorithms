class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(self.V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def isCyclicUtil(self, v, visited, tempStack):
        visited[v] = True
        tempStack[v] = True

        for next in self.graph[v]:
            if visited[next] == False:
                if self.isCyclicUtil(next, visited, tempStack) == True:
                    return True
            elif tempStack[next] == True:
                return True

        tempStack[v] = False
        return False


    def isCyclic(self):
        visited = [False] * self.V
        tempStack =  [False] * self.V

        for edge in range(self.V):
            if visited[edge] == False:
                if self.isCyclicUtil(edge, visited, tempStack) == True:
                    return True

        return False

# g = Graph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
# if g.isCyclic() == 1:
#     print("Graph 1 has a cycle")
# else:
#     print("Graph 1 has no cycle")


g2 = Graph(9)
g2.addEdge(0,1)
g2.addEdge(0,2)
g2.addEdge(1,3)
g2.addEdge(1,5)
g2.addEdge(3,4)
g2.addEdge(2,6)
g2.addEdge(7,2)
g2.addEdge(2,8)

if g2.isCyclic() == 1:
    print("Graph 2 has a cycle")
else:
    print("Graph 2 has no cycle")
