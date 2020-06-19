import json
from Graph import Graph


def load_data(file_name):
    if file_name.find('.json') == -1:
        str = '.json'
        file_name += str
    try:
        with open(file_name, 'r') as file:
            json_file_data = json.load(file)
        json_graph = Graph(json_file_data)
    except:
        print('Error while handling file:', file_name)
        return
    return json_graph


def save_data(graph, new_file_name):
    if new_file_name.find('.json') == -1:
        str = '.json'
        new_file_name += str
    try:
        with open(new_file_name, 'w') as file:
            json.dump(graph.serialize(), file)
    except:
        print('Error while handling file:', new_file_name)
        return
    return
