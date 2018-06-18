class Queue():
    def __init__(self):
        self._data = []

    def enqueue(self, data):
        self._data.append(data)
    
    def dequeue(self):
        if len(self._data) == 0:
            raise ValueError('Cannot remove element from empty queue')
        else:
            value = self._data[0]
            del self._data[0]
            return value
    
    def isEmpty(self):
        return len(self._data) == 0

    def length(self):
        return len(self._data)
    
    def first(self):
        if len(self._data) == 0:
            raise ValueError('Empty queue')
        else:
            return self._data[0]


queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
print('first', queue.first())
print(queue.dequeue())
print('first', queue.first())
print(queue.dequeue())
print(queue.dequeue())