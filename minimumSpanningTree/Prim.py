import sys

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for i in range(V) ] for j in range(V)]

    def add_egde(self, x, y, weight):
        self.graph[x][y] = weight
        self.graph[y][x] = weight

    def printMST(self, parent):
        for x in range(1, self.V):
            print("{}--{}=>{}".format(x,parent[x],self.graph[x][parent[x]]))

    def min_index(self, arr, mstSet):
        min = sys.maxsize
        for x in range(self.V):
            if arr[x] < min and mstSet[x] == False:
                min = arr[x]
                min_index = x

        return min_index

    def prim(self):

        parent = [0] * self.V
        weights = [sys.maxsize] * self.V
        mstSet = [False] * self.V

        parent[0] = -1
        weights[0] = 0

        for c in range(self.V):

            mi = self.min_index(weights, mstSet)
            mstSet[mi] = True

            for s in range(self.V):
                if self.graph[mi][s] > 0 and mstSet[s] == False and weights[s] > self.graph[mi][s]:
                    weights[s] = self.graph[mi][s]
                    parent[s] = mi
        self.printMST(parent)

if __name__ == "__main__":
    g = Graph(6)
    g.add_egde(0,2,2)
    g.add_egde(0,1,1)
    g.add_egde(1,3,4)
    g.add_egde(1,2,3)
    g.add_egde(2,4,2)
    g.add_egde(4,5,4)
    g.add_egde(3,5,3)
    g.add_egde(2,3,1)
    g.add_egde(1,4,1)

    # print(g.graph[3])

    # g.min_index(g.graph[3], [False, False, False, False, False, False]) # before creating mstSet
    g.prim()