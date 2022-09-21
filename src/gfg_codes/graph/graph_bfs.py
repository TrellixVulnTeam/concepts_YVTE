"""
Breadth First Traversal of a un-directed graph

Time complexity: O(V+E)


"""

from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, u, v):
        """
        Assuming un-directed graph
        """
        self.graph[u].add(v)
        self.graph[v].add(u)

    def bfs(self, s: int):
        list_bfs = []
        queue = []

        # +1 to account for 1-indexed (just in case)
        arr_visited = [False] * (max(self.graph.keys()) + 1)

        arr_visited[s] = True
        queue.append(s)

        while len(queue) > 0:
            curr_node = queue.pop(0)
            list_bfs.append(curr_node)

            for node in self.graph[curr_node]:
                if not arr_visited[node]:
                    queue.append(node)
                    arr_visited[node] = True

        return list_bfs

    def bfs_disconn(self, s):
        list_all_bfs = []
        num_vertices = max(self.graph.keys()) + 1
        arr_visited = [False] * (num_vertices)

        list_bfs = self.bfs(s)
        for node in list_bfs:
            arr_visited[node] = True
        list_all_bfs.extend(list_bfs)

        for ith in range(num_vertices):
            if not arr_visited[ith]:
                list_bfs = self.bfs(ith)
                for node in list_bfs:
                    arr_visited[node] = True

                list_all_bfs.extend(list_bfs)

        return list_all_bfs


def main():
    g = Graph()
    list_edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3), (8, 9)]
    for u, v in list_edges:
        g.add_edge(u, v)

    print(g.bfs(2))
    print(g.bfs_disconn(2))


if __name__ == "__main__":
    main()
