import take_a_walk.midtown_graph as mg
import take_a_walk.traverse as t
#! /usr/bin/env python


data = mg.read_midtown_graph_data(49, 1, 'NE', 56, 3, 'NE')
graph = mg.convert_data_to_graph(data)
start = mg.Node(data['start']['posX'], data['start']['posY'])
finish = mg.Node(data['finish']['posX'], data['finish']['posY'])

path = t.bfs_path(graph, start, finish)

mg.display_graph_networkx(graph, path)



