class Stack:
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._capacity

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()

    def push(self, e):
        if self.is_full():
            raise Exception('Stack is full')
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]


stack1 = Stack(capacity=5)

stack1.push(1)

stack1.push(2)

print(stack1.is_full())

print(stack1.top())

print(stack1.pop())

print(stack1.top())

print(stack1.pop())

print(stack1.is_empty())
