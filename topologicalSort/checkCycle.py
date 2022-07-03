# The logic to to try is this:
# start going though the dfs
# keep a stack for the ones that you are currently going trough
# keep a boolean for checking if the process is still going on
# if the process has not yet ended and you find a node vertex that is visited
# that means there is a cycle


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[] for i in range(self.V)]


    def print_graph(self):
        print(self.graph)


    def add_adge(self, s, e):
        self.graph[s].append(e)




if __name__ == "__main__":
    g = Graph(6)
    g.add_adge(0,2)
    g.add_adge(0,1)

    g.print_graph()

# graph1 = {0:{2,1}, 1:{2,4,3}, 2:{0}, 3:{4}, 4:{5}, 5:{3}} # cycle
# graph2 = {0:{1,2}, 1:{5,3}, 2:{6,8}, 3:{4}, 4:{}, 5:{}, 6:{}, 7:{2}, 8:{}} # no cycle

# cycleCheck(graph2)