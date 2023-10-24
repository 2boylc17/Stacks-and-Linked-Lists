import Node


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


list1 = LinkedList()
n1 = Node1("Fred")
n2 = Node1("Tom")
n1.link(n2)
list1.add(n1)
