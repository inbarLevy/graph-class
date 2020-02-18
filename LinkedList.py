class Node:
    def __init__(self, data):
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.vertex_dict = {}

    def add_new_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if data not in self.vertex_dict:
            self.vertex_dict[data] = data

    def del_vertex_from_dict(self, vertex):
        del self.vertex_dict[vertex]