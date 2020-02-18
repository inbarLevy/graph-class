from LinkedList import LinkedList
from collections import deque


# section A:
class Graph:
    # new Complexity Time: O(V+E)
    def __init__(self, dict):
        self.hashTable_linkedList = Graph.hashTable_to_graph(dict)

    @staticmethod
    def hashTable_to_graph(dict):
        graph = {}
        for vertex in dict.keys():
            if type(vertex) == str:
                if vertex not in graph.keys():
                    graph[vertex] = LinkedList()
                for next_vertex in dict[vertex]:
                    if next_vertex == vertex or type(next_vertex) != str:
                        print("couldn't add " + str(next_vertex) + ' to ' + vertex)
                    elif next_vertex not in graph[vertex].vertex_dict:
                        graph[vertex].add_new_node(next_vertex)
                        if next_vertex not in graph.keys():
                            graph[next_vertex] = LinkedList()
                        graph[next_vertex].add_new_node(vertex)
            else:
                print("invalid value, couldn't add " + str(vertex) + " to graph")
        return graph

    # section C.7
    @staticmethod
    def deserialize(dict):
        graph = Graph(dict)
        return graph

    # section A:
    def get_vertices(self):
        return list(self.hashTable_linkedList.keys())

    # section A:
    def get_edges(self):
        edges = []
        for vertex in self.hashTable_linkedList:
            next_vertex = self.hashTable_linkedList[vertex].head
            while next_vertex:
                if {vertex, next_vertex.data} not in edges:
                    edges.append({vertex, next_vertex.data})
                next_vertex = next_vertex.next
        return edges

    # section A:
    def BFS(self, start, goal):
        try:
            x = (start, [start])
            queue = deque()
            queue.append(x)
            results = []
            while queue:
                (vertex, path) = queue.popleft()
                for next in set(self.hashTable_linkedList[vertex].vertex_dict.keys()) - set(path):
                    if next == goal:
                        results.append(path + [next])
                    else:
                        queue.append((next, path + [next]))
            return results
        except:
            print("incorrect values, couldn't find path")
            return

    # section C.1
    def delete_vertex(self, unwanted_vertex):
        if unwanted_vertex not in self.hashTable_linkedList:
            print('vertex does not exist in graph')
            return
        else:
            del self.hashTable_linkedList[unwanted_vertex]
            for vertex in self.hashTable_linkedList:
                if unwanted_vertex in self.hashTable_linkedList[vertex].vertex_dict:
                    self.hashTable_linkedList[vertex].del_vertex_from_dict(unwanted_vertex)
                    vertex_1 = self.hashTable_linkedList[vertex].head
                    if vertex_1.data == unwanted_vertex:
                        self.hashTable_linkedList[vertex].head = vertex_1.next
                    elif vertex_1.next:
                        vertex_2 = self.hashTable_linkedList[vertex].head
                        vertex_2 = vertex_2.next
                        if vertex_2.data == unwanted_vertex:
                            vertex_1.next = vertex_2.next
                        else:
                            while vertex_2.next:
                                if vertex_2.data == unwanted_vertex:
                                    vertex_1.next = vertex_2.next
                                    vertex_2.next = None
                                else:
                                    vertex_1 = vertex_2
                                    vertex_2 = vertex_2.next

    # section C.2
    def add_vertex(self, new_vertex, new_vertex_list):
        if type(new_vertex) == str:
            if new_vertex not in self.hashTable_linkedList.keys():
                self.hashTable_linkedList[new_vertex] = LinkedList()
            for next_vertex in new_vertex_list:
                if next_vertex == new_vertex or type(
                        next_vertex) != str or next_vertex not in self.hashTable_linkedList.keys():
                    print("couldn't add " + str(next_vertex) + ' to ' + new_vertex)
                elif new_vertex not in self.hashTable_linkedList[next_vertex].vertex_dict or \
                        next_vertex not in self.hashTable_linkedList[new_vertex].vertex_dict:
                    print(self.hashTable_linkedList[next_vertex].vertex_dict)
                    self.hashTable_linkedList[new_vertex].add_new_node(next_vertex)
                    self.hashTable_linkedList[next_vertex].add_new_node(new_vertex)
                    print(self.hashTable_linkedList[next_vertex].vertex_dict)
        else:
            print("invalid value, couldn't add " + str(new_vertex) + " to graph")

    # section C.3
    def reverse_path(self, start, goal):
        try:
            x = (start, [start])
            queue = deque()
            queue.append(x)
            results = []
            while queue:
                (vertex, path) = queue.popleft()
                for next in set(self.hashTable_linkedList[vertex].vertex_dict.keys()) - set(path):
                    if next == goal:
                        results.append([next] + path)
                    else:
                        queue.append((next, [next] + path))
            return results
        except:
            print("incorrect values, couldn't find path")
            return

    # section C.4
    def shortest_path(self, start, goal):
        results = self.BFS(start, goal)
        if results:
            shortest_results = []
            min = len(results[0])
            for i in range(len(results)):
                if len(results[i]) == min:
                    shortest_results.append(results[i])
                    min = len(results[i])
                elif len(results[i]) < min:
                    shortest_results = results[i]
                    min = len(results[i])
            return shortest_results
        elif len(results) == 0:
            print('requested path does not exist')

    # section C.5
    def get_center_from_shortest_path(self, start, goal):
        results = self.shortest_path(start, goal)
        if results:
            if len(results) == 0:
                print('requested path does not exist')
            else:
                center_list = []
                for result in range(len(results)):
                    num_of_vertex = len(results[result])
                    list_of_vertex = results[result]
                    if num_of_vertex % 2 != 0:
                        center_list.append([list_of_vertex[int((num_of_vertex / 2))]])
                    else:
                        centers = [list_of_vertex[int((num_of_vertex / 2) - 1)],
                                   list_of_vertex[int((num_of_vertex / 2))]]
                        center_list.append(centers)
                return center_list

    # section C.6
    def serialize(self):
        hash_table = {}
        for vertex in self.get_vertices():
            hash_table[vertex] = list(self.hashTable_linkedList[vertex].vertex_dict.keys())
        return hash_table
