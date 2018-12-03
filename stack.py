"""
The only deviation with this stack compared to a normal one is that it has a print method on it, which I think simplifies debugging code.
"""


class Stack:
    def __init__(self):
        self.__item = {}
        self.current_length = 0

    def isEmpty(self):
        return self.__item == {}

    def push(self, item):
        self.current_length += 1
        self.__item[self.current_length] = item

    def pop(self):
        top = self.__item.pop(self.current_length)
        self.current_length -= 1
        return top

    def peek(self):
        #if self.isEmpty:
         #   raise KeyError("Cannot peek an empty stack")
        return self.__item[self.current_length]

    def size(self):
        return self.current_length

    def __len__(self):
        return self.size()
    
    def __str__(self):
        allItems = []
        for item in self.__item:
            items = str(self.__item[item])
            allItems.append(items)
        return ', '.join(allItems)
