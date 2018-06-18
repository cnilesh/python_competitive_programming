class QueueCircularArr():

    def __init__(self, size):
        self._data = [None] * size
        self._front = 0
        self._size = size
        self.curr_len = 0

    def enqueue(self, data):
        if self.curr_len == self._size:
            raise ValueError('Cannot add element to already populated queue')
        self._data[((self._front+self.curr_len) % (self._size))] = data
        self.curr_len += 1

    def dequeue(self):
        if len(self._data) == 0:
            raise ValueError('Cannot remove element from an empty queue')
        else:
            value = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % (self._size)
            self.curr_len -= 1
            print(self._data)
            return value

queue = QueueCircularArr(3)
queue.enqueue(5)
queue.enqueue(6)
print(queue.dequeue())
queue.enqueue(7)
queue.enqueue(8)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())