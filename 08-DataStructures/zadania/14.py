class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0

import random
a = Stack()
for i in range(5):
    a.push(random.randrange(1,10))
for i in range(3):
    print(a.pop())
