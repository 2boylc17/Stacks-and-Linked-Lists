class Stack:
    def __init__(self, capacity):
        self.internalArray = [None] * capacity
        self.index = 0
        self.capacity = capacity

    def push(self, item):
        # Code to add an item to the stack will go here
        if self.index < self.capacity:
            self.internalArray[self.index] = item
            self.index = self.index + 1
            print(f"{self.internalArray[self.index - 1]} has been added at index {self.index - 1}")
        else:
            print("Stack is full")
        pass  # ends the method when it's empty

    def pop(self):
        # Code to remove an item from the top of the stack will go here
        if self.index == 0:
            print("Stack is empty")
        else:
            removed = self.internalArray[self.index - 1]
            self.internalArray[self.index - 1] = None
            self.index = self.index - 1
            return print(f"{removed} was removed")
        pass  # ends the method when it's empty

    def __str__(self):
        return self.internalArray.__str__()


stack1 = Stack(5)
stack1.push("yes")
stack1.push("yes")
stack1.push("yes")
stack1.push("yes")
stack1.push("yes")
stack1.push("yes")
print(stack1)
stack1.pop()
