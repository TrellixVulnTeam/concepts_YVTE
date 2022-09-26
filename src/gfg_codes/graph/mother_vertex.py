"""
https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        for node in self.graph[v]:
            if not visited[node]:
                self.DFSUtil(node, visited)

        visited[v] = True

    def find_mother_vertex(self):
        visited = [False] * max(self.graph.keys())

        mother_vertex = -1
        for node in self.graph.keys():
            if not visited[node]:
                self.DFSUtil(node, visited)
                mother_vertex = node

        visited = [False] * max(self.graph.keys())
        self.DFSUtil(mother_vertex, visited)

        if all(not visited_i for visited_i in visited):
            mother_vertex = -1

        return mother_vertex


def main():
    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)

    # Function call
    print("A mother vertex is " + str(g.find_mother_vertex()))


if __name__ == '__main__':
    main()
