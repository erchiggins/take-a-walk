import networkx as nx 

class QueueNode(object):
    def __init__(self, node):
        self.node = node
        self.prevNode = None #closer to head of queue
        self.nextNode = None #closer to tail of queue

class BFSQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        popped = self.head
        if popped:
            # there was at least one item in the queue
            # reassign head to next in queue, if it exists
            if self.head.nextNode:
                self.head = self.head.nextNode
                # remove reference to former head of queue
                self.head.prevNode = None
            else:
                self.head = None
                self.tail = None
        return popped

    def add(self, node):
        # assign node to nextNode after former tail
        if self.tail:
            # queue is not empty
            self.tail.nextNode = node
            # assign former tail to prevNode of new tail
            node.prevNode = self.tail
            # set tail to be new node
            self.tail = node
        else:
            #queue was empty and needs 
            self.tail = node
            self.head = node


# this will not give the shortest path in a weighted graph 
# done as an exercise
def bfs_path(graph, start, finish):
    # track which node was visited before the current node
    parent = {}
    # nodes to visit
    frontier = BFSQueue()
    parent[start] = None
    frontier.add(QueueNode(start))

    while frontier.head is not None:
        to_explore = frontier.pop()
        # is it the node we're looking for
        if to_explore.node == finish:
            break
        # ok, if not, look at its neghbors 
        for n in graph.adj[to_explore.node]:
            # check whether each neighbor has been accessed by another node already
            if n not in parent:
                parent[n] = to_explore.node
                frontier.add(QueueNode(n))
    
    # construct path from parent dict, if finish was found
    path = []
    if finish in parent:
        current_node = finish
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]
    return path

def dijkstra_path(graph):
    pass
