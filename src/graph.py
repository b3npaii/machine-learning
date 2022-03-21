from queues import Queue
from queues import Stack

class Node:

    def __init__(self, index):
        self.index = index
        self.distance = 0
        self.previous = None

class graph:
    def __init__(self, edges):
        self.edges = edges
        self.num_edges = len(edges)
        self.nodes = {}
        for edge in edges:
            if edge[0] not in self.nodes:
                self.nodes[edge[0]] = Node(edge[0])
            if edge[1] not in self.nodes:
                self.nodes[edge[1]] = Node(edge[1])

    def get_parents(self, child):
        parents = []
        for i in range(0, self.num_edges):
            if self.edges[i][1] == child:
                parents.append(self.edges[i][0])
        return parents

    def get_children(self, parent):
        children = []
        for i in range(0, self.num_edges):
            if self.edges[i][0] == parent:
                children.append(self.edges[i][1])
        return children

    def breadth_first(self, start):
        queue = Queue([start])
        seen = {}
        order = []
        while queue.line != []:
            dequeued = queue.dequeue()
            order.append(dequeued)
            seen[dequeued] = True
            children = self.get_children(dequeued)
            if children is None:
                continue
            for child in children:
                if child in seen:
                    continue
                queue.enqueue(child)
                seen[child] = True
        return order
    
    def depth_first(self, start):
        stack = Stack([start])
        seen = {}
        order = []
        while stack.data != []:
            destacked = stack.pop()
            order.append(destacked)
            seen[destacked] = True
            children = self.get_children(destacked)
            for child in children:
                if children == None:
                    continue
                elif child in seen:
                    continue
                stack.push(child)
                seen[child] = True
        return order

    def set_distance_and_previous(self, start_index):
        queue = Queue([start_index])
        visited = {}
        order = [start_index]
        while len(queue.line) != 0:
        
            current_node = queue.line[0]
            order.append(current_node)
            visited.update({current_node: True})
            queue.dequeue()
            children = self.get_children(current_node)
            node = self.nodes[current_node]

            for child in children:
                if child in visited:
                    continue
                self.nodes[child].previous = current_node
                self.nodes[child].distance = self.nodes[current_node].distance + 1
                queue.enqueue(child)
                visited.update({child: True})
        return order 
    
    def calc_distance(self, start_index, ending_index):
        self.set_distance_and_previous(start_index)
        if ending_index not in self.set_distance_and_previous(start_index):
            return False
        else: 
            return self.nodes[ending_index].distance
    
    def calc_shortest_path(self, start_index, ending_index): 
        self.set_distance_and_previous(start_index)

        if self.calc_distance(start_index, ending_index) == False: 
            return False 
        
        shortest_path = []
        start_node_index = start_index
        current_node_index = ending_index
    
        while current_node_index != start_node_index: 
            shortest_path.append(current_node_index)
            current_node_index = self.nodes[current_node_index].previous
            shortest_path.append(current_node_index)

        shortest_path = list(dict.fromkeys(shortest_path))
        return shortest_path[::-1]
    
   # def calc_distance(x, y):
a = graph([[0, 1], [1, 2], [1, 4], [4, 5], [4, 3], [3, 1], [3, 6]])
a.set_distance_and_previous(1)
print(a.calc_shortest_path(1, 6))
print(a.calc_distance(1, 6))