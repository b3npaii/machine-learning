from queues import Queue
from queues import Stack
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

    def breadth_first(self, start):
        queue = Queue([start])
        seen = {}
        order = []
        while queue != []:
            dequeued = queue.dequeue()
            print(dequeued)
            order.append(dequeued)
            seen[dequeued] = True
            children = self.get_children(dequeued)
            for child in children:
                if children == None:
                    continue
                elif child in seen:
                    continue
                queue.enqueue(child)
                seen[child] = True
        return order
    
    def depth_first(self, start):
        stack = Stack([start])
        seen = {}
        order = []
        while len(stack) > 0:
            destacked = stack.pop()
            order.append(destacked)
            seen[destacked] = True
            children = self.get_children(dequeued)
            for child in children:
                if children == None:
                    continue
                elif child in seen:
                    continue
                stack.push(child)
                seen[child] = True
        return order
