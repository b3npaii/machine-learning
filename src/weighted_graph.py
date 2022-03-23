from graph import *

class WeightedGraph(graph):
    
    def __init__(self, weights):
        self.weights = weights

        edges = []
        for weight in weights:
            edges.append(weight)
        super().__init__(edges)

    def calc_distance(self, start_index, ending_index):
        for node_index in self.nodes:
            if node_index == start_index: 
                continue
            else: 
                self.nodes[node_index].distance = 99999

        current_node_index = start_index
        visited_nodes = []
        distances = {}

        while current_node_index != ending_index:

            if current_node_index in visited_nodes:
                distances.pop(current_node_index)
        
            visited_nodes.append(current_node_index)

            for children_index in self.get_children(current_node_index):
                if children_index in visited_nodes:
                    continue
                self.nodes[children_index].distance = min(self.nodes[children_index].distance, self.nodes[current_node_index].distance + self.weights[(current_node_index, children_index)])
                distances[children_index] = self.nodes[children_index].distance

            min_distance_index = min(distances, key=distances.get)

            current_node_index = min_distance_index

        return self.nodes[ending_index].distance
    
    def calc_shortest_path(self, start_index, ending_index): 
        
        self.calc_distance(start_index, ending_index)

        shortest_path_edges = []
        for edges in self.edges: 
            node_a_distance = self.nodes[edges[0]].distance
            node_b_distance = self.nodes[edges[1]].distance
            if node_b_distance - node_a_distance == self.weights[edges]:
                shortest_path_edges.append(edges)
                shortest_path_edges.append(edges[::-1])

        shortest_graph = graph(shortest_path_edges)
        return shortest_graph.calc_shortest_path(start_index, ending_index)