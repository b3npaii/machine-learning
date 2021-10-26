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
a = graph([[1, 2], [1, 3], [1, 5], [0, 1,], [0, 9], [5, 8], [5, 2]])
print(a.get_children(1))
print(a.get_parents(2))