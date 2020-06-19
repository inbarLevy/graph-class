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


# create list of random letters
optional_vertices_list = get_optional_vertices_list()

# crate a dictionary from the list of random letters
rand_dict = create_rand_dict(optional_vertices_list)

# create a Graph object from the dictionary
rand_graph = Graph(rand_dict)

# add new vertex to the graph
rand_graph.add_vertex(find_random_letter(), get_rand_vertices_list(optional_vertices_list))

# save the new vertices of the graph
vertices = rand_graph.get_vertices()

# save the new edges of the graph
rand_vertex = vertices[random.randint(0, len(vertices) - 1)]

# delete vertex from the graph
rand_graph.delete_vertex(rand_vertex)

# Save the new graph to the new_graph.json file
files_functions.save_data(rand_graph, 'new_graph.json')

print(Graph.deserialize(rand_dict))