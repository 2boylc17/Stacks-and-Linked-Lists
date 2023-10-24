class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return self.data.__str__()

    def link(self, newnode):
        self.next = newnode
        newnode.prev = self


"""n1 = Node("Fred")
n2 = Node("Tom")
n1.link(n2)
"""