from functools import reduce
import operator


class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items is []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    @property
    def str(self):
        t = len(self.items) - 1
        return reduce(operator.add, self.items[0:t])

    @property
    def str_full(self):
        return reduce(operator.add, self.items)