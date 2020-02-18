from Graph import Graph
import files_functions
import string
import random


# assist functions:
def find_random_letter():
    return random.choice(string.ascii_letters)


def get_optional_vertices_list():
    rand_vertex_list = []
    for i in range(random.randint(0, 53)):
        temp = find_random_letter()
        if temp not in rand_vertex_list:
            rand_vertex_list.append(temp)
    return rand_vertex_list


def get_rand_vertices_list(optional_vertices_list):
    rand_list = []
    for i in range(random.randint(0, len(optional_vertices_list))):
        rand_list.append(optional_vertices_list[i])
    return rand_list


def create_rand_dict(optional_vertices_list):
    rand_dict = {}
    for i in range(random.randint(0, len(optional_vertices_list))):
        temp = optional_vertices_list[i]
        if temp not in rand_dict.keys():
            rand_dict[temp] = get_rand_vertices_list(optional_vertices_list)
    return rand_dict


# section 4:
optional_vertices_list = get_optional_vertices_list()
rand_dict = create_rand_dict(optional_vertices_list)
rand_graph = Graph(rand_dict)

# section 4.1:
print(rand_graph.get_vertices())

# section 4.2:
print(rand_graph.get_edges())

# section 4.3:
rand_graph.add_vertex(find_random_letter(), get_rand_vertices_list(optional_vertices_list))

# section 4.4:
print(rand_graph.get_vertices())

# section 4.5:
vertices = rand_graph.get_vertices()
rand_vertex = vertices[random.randint(0, len(vertices) - 1)]
rand_graph.delete_vertex(rand_vertex)

# section 4.6:
print(rand_graph.get_vertices())

# section 4.7:
files_functions.save_data(rand_graph,'new_graph.json')
