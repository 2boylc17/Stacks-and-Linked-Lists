class Node1:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return self.data.__str__()

    def link(self, newnode):
        self.next = newnode
        newnode.prev = self


"""n1 = Node1("Fred")
n2 = Node1("Tom")
n1.link(n2)
"""