import json
import requests
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Node:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def __eq__(self, other):
        return self.posX == other.posX and self.posY == other.posY

    def __hash__(self):
        return hash((self.posX, self.posY))


base_url = 'http://graphattan.us-west-1.elasticbeanstalk.com/graph?'


def read_midtown_graph_data(start_st, start_ave, start_corner, finish_st, finish_ave, finish_corner):
    url = base_url + \
        f'start_st={start_st}&start_ave={start_ave}&start_corner={start_corner}&finish_st={finish_st}&finish_ave={finish_ave}&finish_corner={finish_corner}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def convert_data_to_graph(data):
    graph = nx.MultiGraph()
    for item in data['graph']:
        vertex = item['vertex']
        for edge in item['edges']:
            source = Node(vertex['posX'], vertex['posY'])
            destination = Node(edge['destination']['posX'],
                               edge['destination']['posY'])
            graph.add_edge(source, destination,
                           weight=edge['weight'], type=edge['type'])
    return graph


def display_graph_networkx(graph, path):
    positions = {n: (n.posX, n.posY) for n in graph.nodes()}
    node_colors = ['red' if node in path else 'black' for node in graph.nodes()]
    edge_colors = ['blue' if edge[2]['type'] ==
                   'SIDEWALK' else 'purple' for edge in graph.edges(data=True)]
    nx.draw_networkx(graph, pos=positions, edge_color=edge_colors,
                     with_labels=False, node_color=node_colors, node_size=10)
    plt.show()

