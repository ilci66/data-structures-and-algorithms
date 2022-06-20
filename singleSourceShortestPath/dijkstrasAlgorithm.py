import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def add_egde(self, s, e, distance):
		self.graph[s][e] = distance
		self.graph[e][s] = distance

	def printSolution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	def minDistance(self, distances, sptSet):
		min = sys.maxsize
		for x in range(self.V):
			if distances[x] < min and sptSet[x] == False:
				min = distances[x]
				min_index = x
		return min_index

	def dijkstra(self, start):

		distances = [sys.maxsize] * self.V
		distances[start] = 0
		sptSet = [False] * self.V

		for time in range(self.V):

			x = self.minDistance(distances, sptSet)
			sptSet[x] = True

			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False \
						and distances[y] > distances[x] + self.graph[x][y]:
					distances[y] = distances[x] + self.graph[x][y]

		return self.printSolution(distances)

if __name__ == "__main__":

	g = Graph(9)
	g.add_egde(0,1,3)
	g.add_egde(0,3,2)
	g.add_egde(1,2,1)
	g.add_egde(2,3,4)
	g.add_egde(2,4,3)
	g.add_egde(1,4,8)
	g.add_egde(5,4,2)
	g.add_egde(1,5,4)
	g.add_egde(3,7,12)
	g.add_egde(6,5,3)
	g.add_egde(8,5,6)
	g.add_egde(6,8,2)
	g.add_egde(7,6,11)
	print(g.graph)

	g.dijkstra(0)
