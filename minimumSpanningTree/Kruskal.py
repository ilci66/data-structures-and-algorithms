# IT'S NOT WORKING PROPERLY YET

class Graph:
    def __init__(self, vertices):
        self.V = vertices # important because the algorith will run V-1 times
        self.graph = [] 


    def add_edge(self, s, e, weight):
        self.graph.append([s,e,weight])


    def find(self, parent, i):
        if parent[i] == -1:
            return i
        self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)

        if rank[rootX] > rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] < rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootX] = parent[rootY]
            rank[rootX] += 1

    def kruskal(self):

        self.graph = sorted(self.graph, key = lambda item: item[-1])
        print(self.graph)

        parent = [-1] * self.V
        rank = [0] * self.V
        result = [] # Array to print after the algorithm is done

        e = 0 # This many times I will add
        i = 0 # To check all the edges, for cycles too

        while e < self.V -1:
            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # continue if they don't form a cycle
            if x != y:
                result.append([u,v,w])
                self.union(parent, rank, x, y)
                e += 1

        for k in result:
            print("{} -- {} ==> {}".format(k[0], k[1], k[2]))



if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5,3,4)
    g.add_edge(5,4,3)
    g.add_edge(4,2,1)
    g.add_edge(4,3,2)
    g.add_edge(1,3,1)
    g.add_edge(2,1,3)
    g.add_edge(0,1,1)
    g.add_edge(0,2,2)

    for x in range(len(g.graph)):
        print(g.graph[x])
    # Function call
    g.kruskal()

# This code is contributed by Neelam Yadav
