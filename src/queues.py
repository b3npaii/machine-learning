class Queue:
    def __init__(self, contents):
        self.line = [contents]

    def print(self):
        for i in self.line:
            print(i)

    def enqueue(self, item):
        self.line.append(item)

    def dequeue(self):
        return self.line.pop(0)

class Stack:
    def __init__(self, contents):
        self.data = []

    def print(self):
        reversed = self.data[::-1]
        for i in reversed:
            print(i)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop(len(self.data) - 1)