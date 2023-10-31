class Queue:
    def __init__(self, capacity):
        self.internalArray = [None] * capacity
        self.front = 0
        self.back = 0
        self.capacity = capacity

    def add(self, item):
        if self.internalArray[self.back] is not None:
            print("Queue is full")
        else:
            self.internalArray[self.back] = item
            self.back = self.back + 1
            if self.back == self.capacity:
                self.back = 0
            print(f"Added {item} to queue")
        pass

    def remove(self):
        if self.internalArray[self.front] is not None:
            removed = self.internalArray[self.front]
            self.internalArray[self.front] = None
            self.front = self.front + 1
            if self.front == self.capacity:
                self.front = 0
            return print(f"{removed} has been removed from the queue")
        pass

    def __str__(self):
        return self.internalArray.__str__()


stack1 = Queue(5)
stack1.add("1")
print(stack1)
stack1.add("2")
print(stack1)
stack1.add("3")
print(stack1)
stack1.add("4")
print(stack1)
stack1.add("5")
print(stack1)
stack1.add("6")
print(stack1)
stack1.remove()
print(stack1)
stack1.remove()
print(stack1)
stack1.add("7")
print(stack1)
