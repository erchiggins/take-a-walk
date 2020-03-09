import take_a_walk.midtown_graph as mg
import take_a_walk.traverse
#! /usr/bin/env python


data = mg.read_midtown_graph_data(22, 7, 'SE', 53, 4, 'SW')
graph = mg.convert_data_to_graph(data)
start = mg.Node(data['start']['posX'], data['start']['posY'])
finish = mg.Node(data['finish']['posX'], data['finish']['posY'])

visited = []

mg.display_graph_networkx(graph, start, finish)

