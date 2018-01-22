"""
This is simply a generic queue I implemented with a dictionary. I believe it was written as an assignment in my first data structures course.
"""


class Queue:
    def __init__(self):
        self.__items = {}
        self.bottom = 0
        self.top = 0

    def isEmpty(self):
        return self.__items == {}

    def enqueue(self, item):
        self.__items[self.bottom] = item
        self.bottom += 1

    def dequeue(self):
        if self.bottom == 0:
            raise ValueError('The Queue is empty')
        rm = self.__items.pop(self.top)
        self.top += 1
        return rm

    def size(self):
        return len(self.__items)
