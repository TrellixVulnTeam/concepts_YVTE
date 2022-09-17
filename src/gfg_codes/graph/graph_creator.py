class AdjNode:
    """
    Holds a node value and pointer to the next node
    """

    def __init__(self, node_val):
        self.node_val = node_val
        self.next = None


class AdjGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # List of pointers to AdjNodes
        self.adj_graph = [None] * self.num_vertices

    def add_edge(self, src_node_val, dst_node_val):
        # Create node objects
        src_node = AdjNode(src_node_val)
        dst_node = AdjNode(dst_node_val)

        # Append the linked list pointed by dst_node's pointer to src_node's next
        # And, then point dst_node's pointer to src_node making it the new head
        src_node.next = self.adj_graph[dst_node_val]
        self.adj_graph[dst_node_val] = src_node

        dst_node.next = self.adj_graph[src_node_val]
        self.adj_graph[src_node_val] = dst_node

    def __repr__(self):
        str_repr = ""
        for v_index, adj_node in enumerate(self.adj_graph):
            str_repr += f"\nNode {v_index}: "
            while adj_node is not None:
                str_repr += f"-> {adj_node.node_val} "
                adj_node = adj_node.next
        return str_repr


def create_graph(num_vertices, list_edges):
    obj_graph = AdjGraph(num_vertices)
    for edge in list_edges:
        src, dst = edge
        obj_graph.add_edge(src, dst)

    return obj_graph


def main():
    num_vertices = 5
    list_edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    obj_graph = create_graph(num_vertices, list_edges)
    print(obj_graph)


if __name__ == '__main__':
    main()
