# The link for the strategy for brute force can be found here
# use it to create the logic
# https://www.youtube.com/watch?v=Rs6DXyWpWrI

# TODO: Find all pairs shortest path using Floyd Warshall algo.

# TODO: Check if between any two pairs, the distance is infinite,
#  except self loops

import sys

V = 4
inf = sys.maxsize


def f_w(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    # list(map(lambda i: print("i => ", i), graph))
    # list(map(lambda i: list(map(lambda j: print("j => ", j), i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][j] + dist[k][j])

    # print_solution(dist)
    return dist


def dfs(graph, visited, v):
    visited[v] = True
    print("v is ==> ", v)

    for j in range(len(graph[v])):
        if not visited[j] and graph[v][j] > 0 and graph[v][j] < sys.maxsize:
            dfs(graph, visited, j)


def print_solution(dist):
    print("Matrices of shortest distances")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == inf:
                print("inf", end=" - ")
            else:
                print(dist[i][j], end=' - ')
            if j == V - 1:
                print(" ")
        # print("--")

def scc(graph):
    g = f_w(graph)
    visited = [False] * len(g)
    dfs(g, visited, 0)


G = [[0, 13, inf, 15],
     [12, 0, inf, 14],
     [inf, 11, 0, 12],
     [inf, 11, 12, 0]]

scc(G)
