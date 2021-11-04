class Queue:
    def __init__(self, contents):
        self.line = contents

    def print(self):
        for i in self.line:
            print(i)

    def enqueue(self, item):
        self.line.append(item)

    def dequeue(self):
        return self.line.pop(0)


class Stack:

    def __init__(self, contents=None):

        if contents is None:
            self.data = []

        else:
            self.data = contents

    def print(self):

        for item in self.data[::-1]:

            print(item)

    def push(self, item_to_push):

        self.data.append(item_to_push)

    def pop(self):
        return self.data.pop()