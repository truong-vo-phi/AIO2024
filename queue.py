class Queue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._capacity

    def front(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[0]
        self._data = self._data[1:]
        return answer

    def enqueue(self, e):
        if self.is_full():
            raise Exception('Queue is full')
        self._data.append(e)


queue1 = Queue(capacity=3)

queue1.enqueue(1)

queue1.enqueue(2)

queue1.enqueue(3)

print(queue1.dequeue())

print(queue1.dequeue())

print(queue1.dequeue())

print(queue1.is_empty())
