from Week4.LinkedLists.Node import Node


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, node):
        if self.last is None:
            self.first = node
            self.last = node
        else:
            self.last.link(node)
            self.last = node

    def get(self, index):
        current = self.first
        for count in range(1, index):
            current = current.next
        return print(current)


list1 = LinkedList()
n1 = Node("yes")
n2 = Node("no")
list1.add(n1)
list1.add(n2)
list1.get(1)
