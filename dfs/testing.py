class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, base_node, add):
        pass


if __name__ == "__main__":
    # arr = [None] * 5
    # adjList = {}
    # print(arr)
    # adjList["a"] = "ca"
    # adjList["a"] = ["cas","asd"]
    # print(adjList)
    # print("yep")

    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}

    for i in range(len(set(["2", "1", "3"])-set(["1"]))):
        print(i)
    print(graph,"-------", [None]*2)