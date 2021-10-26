class graph:
    def __init__(self, edges):
        self.edges = edges
        self.num_edges = len(edges)

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
